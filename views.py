from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.authtoken.views  import ObtainAuthToken
from  rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.decorators import api_view,permission_classes
from .models import User,audiofiles,compareaudiofiles
from django.contrib.auth import authenticate,login,logout
import uuid
from getmac import get_mac_address
from getmac import getmac
from getmac import get_mac_address as gma
import netifaces
import base64
from resemblyzer import VoiceEncoder, preprocess_wav
from pathlib import Path
import random
import smtplib
# import audiodiff
import chunk
import filecmp
import urllib
import hashlib
import os
import os.path
from urllib.request import urlretrieve
import subprocess
from django.core.files.base import ContentFile
import random
from django.core.files.storage import FileSystemStorage
import numpy as np
# from resemblyzer import preprocess_wav, VoiceEncoder
# from demo_utils import *
# from itertools import groupby
# from pathlib import Path
# from tqdm import tqdm
# import matplotlib.pyplot as plt
# import numpy as np
# Create your views here.
FFMPEG_BIN = 'ffmpeg'

@api_view(['POST'])
def adduser(request):
    print(request.META)
    # ipadd=request.META.get('REMOTE_ADDR')
    ipadd=request.META.get('HTTP_X_FORWARDED_FOR')
    getmac.PORT = 4200
    print(get_mac_address(ip=ipadd, network_request=True))
    # print(ipadd)
    if request.method=='POST':
        name=request.data.get('name')
        email=request.data.get('email')
        password=request.data.get('password')
        print(password)
        gender=request.data.get('gender')
        print(gender)
        phonenumber=request.data.get('phonenumber')
        # print(phonenumber)
        print(hex(uuid.getnode()))
        # print(netifaces.ifaddresses('wlan0')[netifaces.AF_LINK]['addr'])
        mac=get_mac_address(ip=ipadd, network_request=True)
        print("mac address is",mac)
        print(gma())
        k=User.objects.create_user(email=email,username=name,password=password,gender=gender,phonenumber=phonenumber,macaddress=mac)
        Token.objects.create(user=k)
    return Response(data = {'username':k.username,'response':'Successfully registered a user','token':Token.objects.get(user=k).key})

@api_view(['POST'])
def userlogin(request):
    if request.method == 'POST':
        email=request.data.get('email')
        password=request.data.get('password')
        user = authenticate(request,username=email,password=password)
        token=Token.objects.get(user=user)
        login(request,user)
        return Response({'message':'success','token':token.key,'email':user.email,'id':user.id,'name':user.username})
    else:
        return Response({'status':0})
    
@api_view(['POST'])
def getaudio(request,userid):
    ipadd=request.META.get('HTTP_X_FORWARDED_FOR')
    getmac.PORT = 4200
    mac=get_mac_address(ip=ipadd, network_request=True)
    user=User.objects.get(id=userid)
    data = request.data.get('audio')
    exefile = request.data.get('filename')
    exefile=exefile+".exe"
    # print(data)
    format, imgstr = data.split(';base64,') 
    string1=imgstr[:6]
    print(string1)
    string2=mac[0:2]+mac[3:5]+mac[6:8]+mac[9:11]
    print(string2)
    string3=string1+string2
    print(string3)
    ext = format.split('/')[-1] 
    d = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
    print(d)
    result = ''.join((random.choice(string3)) for x in range(12)) 
    result=result[0:4]+"-"+result[4:8]+"-"+result[8:12]
    print(result)
    # audio=request.FILES['audio_data']
    audiofiles.objects.create(file1=d,macaddress=mac,user=user,productkey=result,exefile=exefile)
    return Response({'productkey':result})
  
@api_view(['POST'])
def downloadsecurity(request,userid):
    ipadd=request.META.get('HTTP_X_FORWARDED_FOR')
    getmac.PORT = 4200
    mac=get_mac_address(ip=ipadd, network_request=True)
    user=User.objects.get(id=userid)
    data = request.data.get('audio')
    productkey = request.data.get('productkey')
    print(productkey)
    format, imgstr = data.split(';base64,') 
    ext = format.split('/')[-1] 
    d = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
    print(d)
    c=FileSystemStorage()
    d1=c.save(d.name,d)
    print(d1)
    details=audiofiles.objects.get(user__id=userid)
    au=details.file1.path
    print(au)
    exefile=details.exefile
    print(exefile)
    user=User.objects.get(id=userid)
    newaudio=compareaudiofiles.objects.create(file1=d,user=user)
    newau=newaudio.file1.path
    fpath = Path(au)
    print(fpath)
    fpath1 = Path(newau)
    print(fpath1)
    wav = preprocess_wav(fpath)
    wav1 = preprocess_wav(fpath1)
    print(wav)
    print(wav1)
    encoder = VoiceEncoder()
    embed = encoder.embed_utterance(wav)
    embed1 = encoder.embed_utterance(wav1)
    utt_sim_matrix = np.inner(embed, embed1)  
    print("similiar",utt_sim_matrix)
    newaudio.delete() 
    if audiofiles.objects.filter(macaddress=mac,productkey=productkey,status="paid").exists() and utt_sim_matrix>.7:
        check=hashlib.md5(open("media/exefile/"+exefile,'rb').read()).hexdigest()
        print(check)
        save_path = "C://Users/Eileen/Downloads/"
        completeName = os.path.join(save_path, exefile)
        print(completeName)
        file1 = open(completeName, "wb")
        print(file1)
        print(type(file1))
        tofile=open("media/exefile/"+exefile,'rb').read()
        print(type(tofile))
        file1.write(tofile)
        check1=hashlib.md5(open("C://Users/Eileen/Downloads/"+exefile,'rb').read()).hexdigest()
        print(check1)
        if check==check1:
            checkstatus="checksum is verified"
        else:
            checkstatus="checksum is not verified"
        print(checkstatus)
        # newaudio.delete()
        details.delete()
        return Response("successfully downloaded")
    else:
        return Response("can't download")

  
@api_view(['POST'])
def comparevoice(request,userid):
    # encoder = VoiceEncoder()
    details=audiofiles.objects.get(id=userid)
    au=details.file1
    print(au)
    data = request.data.get('audio')
    format, imgstr = data.split(';base64,') 
    ext = format.split('/')[-1] 
    d = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
    c=FileSystemStorage()
    d=c.save(d.name,d)
    print(d)
    if d==au:
        return response("ok")
    else:
        return response("ntok")

def checksum(name, ffmpeg_bin=None):
    if ffmpeg_bin is None:
        ffmpeg_bin = ffmpeg_path()
    args = [
        ffmpeg_bin,
        '-i', name,
        '-vn',
        '-f', 's24le',
        '-',
    ]

def ffmpeg_path():
    return os.environ.get('FFMPEG_BIN', FFMPEG_BIN)

@api_view(['POST'])
def sendotp(request):
    email=request.data.get('email')
    print(email)
    user_data=User.objects.filter(email=email).values()
    if user_data:
        otp=random.randint(1000,9999)
        print(otp)
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('softwarepiracycontroller99@gmail.com','software99')
        msg='Hello, your OTP is '+str(otp)
    # otp=str(otp)
        server.sendmail('eileenninan@gmail.com',email,msg)
        server.quit()
        return Response({'status':"email send successfully",'otp':otp,'email':email})
    else:
        return Response("sending email failed",{'otp':otp})

@api_view(['POST'])
def payment(request):
    userid=request.data.get('id')
    details=audiofiles.objects.get(user__id=userid)
    details.status="paid"
    details.save()
    return Response("successfully paid")