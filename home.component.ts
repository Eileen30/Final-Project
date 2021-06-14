import { Component, Input, OnInit, ViewChild } from '@angular/core';
import * as RecordRTC from 'recordrtc';
import { DomSanitizer } from '@angular/platform-browser';
import { AuthserviceService } from '../authservice.service';
import { FileselectComponent } from '../fileselect/fileselect.component';
import { FileserviceService } from '../fileservice.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  recording = false;
  id;
  //Url of Blob
  url;
  error;
  record;
  audiofile;
  imagesBase64:any [] = [];
  productkey;
  software;

  constructor(private domSanitizer: DomSanitizer,private mys: AuthserviceService,private soft: FileserviceService,private router: Router) { }

  ngOnInit(): void {
      this.id=localStorage.getItem('id')
      this.software=this.soft.software;
    //   console.log(this.software)
  }

    //Will use this flag for detect recording
   
    
    sanitize(url:string){
        return this.domSanitizer.bypassSecurityTrustUrl(url);
    }
    /**
     * Start recording.
     */
    initiateRecording() {
        
        this.recording = true;
        let mediaConstraints = {
            video: false,
            audio: true
        };
        navigator.mediaDevices
            .getUserMedia(mediaConstraints)
            .then(this.successCallback.bind(this), this.errorCallback.bind(this));
    }
    /**
     * Will be called automatically.
     */
    successCallback(stream) {
        var options = {
            mimeType: "audio/wav",
            numberOfAudioChannels: 1
        };
        //Start Actuall Recording
        var StereoAudioRecorder = RecordRTC.StereoAudioRecorder;
        this.record = new StereoAudioRecorder(stream, options);
        this.record.record();
    }
    /**
     * Stop recording.
     */
    stopRecording() {
        this.recording = false;
        this.record.stop(this.processRecording.bind(this));
        console.log(this.url)
        // console.log(this.audiofile)
        
        // const sendAudioFile = file => {
        //   const formData = new FormData();
        //   formData.append('audio-file', file);
        //   return fetch('http://localhost:3000/audioUpload', {
        //     method: 'POST',
        //     body: formData
        //   });
        // };
       
    }
    /**
     * processRecording Do what ever you want with blob
     * @param  {any} blob
     * Blog
     */
    processRecording(blob) {
        this.url = URL.createObjectURL(blob);
        this.audiofile =URL.revokeObjectURL(this.url[blob]);
        this.convertToBase64(blob)
        
    }
    /**
     * Process Error.
     */
    errorCallback(error) {
        this.error = 'Can not play audio in your browser';
    }
    getaudio(){

        this.mys.getaudio(this.imagesBase64,this.id,this.software)
        .subscribe(
            res =>
            {
                console.log(res)
                // this.productkey=res.productkey;
                this.soft.productkey=res.productkey;
                this.productkey=this.soft.productkey;
                console.log(this.soft.productkey)
                this.router.navigate(["/payamount"])
            });
           
    }
    convertToBase64(file){
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => {
            console.log(reader.result);
            this.imagesBase64.push(reader.result);
        };
        console.log(this.imagesBase64)
      }

}
