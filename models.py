from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.contrib.auth.hashers import make_password

# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, email, password, **other_fields):
        """
        Create and save a user with the given email and password. And any other fields, if specified.
        """
        if not email:
            raise ValueError('An Email address must be set')
        email = self.normalize_email(email)
        
        user = self.model(email=email, **other_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def _create_user_phone(self, phonenumber, password,otp, **other_fields):
        """
        Create and save a user with the given email and password. And any other fields, if specified.
        """
        if not phonenumber:
            raise ValueError('Phone number is mandatory')
        
        user = self.model(phonenumber=phonenumber,password=password,otp=otp, **other_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_user_phone(self, phonenumber, password,otp, **other_fields):
        other_fields.setdefault('is_staff', False)
        other_fields.setdefault('is_superuser', False)
        return self._create_user_phone(phonenumber, password,otp,**other_fields)

    def create_user(self, email, password=None, **other_fields):
        other_fields.setdefault('is_staff', False)
        other_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **other_fields)

    def create_superuser(self, email, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **other_fields)

class User(AbstractUser):
    username=models.CharField(max_length=100,null=True,blank=True)
    macaddress=models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=50, null=True,blank=True,unique=True)
    phonenumber = models.IntegerField(unique=True)
    TYPE_SELECT = (('male', 'Male'),('female', 'Female'),('others','others'))
    gender=models.CharField(max_length=11,choices=TYPE_SELECT)
    otp=models.IntegerField(null=True,default=None)
    image = models.ImageField(upload_to='profilefotos/',null=True,blank=True)

   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phonenumber']
    objects = UserManager()

    # def get_username(self):
    #     return self.email
    def __str__(self):
        return str(self.username)

class audiofiles(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)    
    file1 = models.FileField(upload_to='',null=True,blank=True)
    exefile=models.CharField(max_length=100,null=True,blank=True)
    macaddress=models.CharField(max_length=100,null=True,blank=True)
    PAYMENT_STATUS = (('paid', 'paid'),('unpaid', 'unpaid'))
    status=models.CharField(max_length=11,choices=PAYMENT_STATUS,default="unpaid")
    productkey=models.CharField(max_length=20,null=True,blank=True)

class compareaudiofiles(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)    
    file1 = models.FileField(upload_to='',null=True,blank=True)