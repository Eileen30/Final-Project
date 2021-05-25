import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ConfigserviceService } from './configservice.service';
import { HttpClient, HttpClientModule } from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class AuthserviceService {
  

  constructor(private _url:ConfigserviceService, private http: HttpClient) { }
  private _adduser=this._url.config_url+"adduser";
  private _login=this._url.config_url+"userlogin";
  private _getaudio=this._url.config_url+"getaudio";
  private _sendotp=this._url.config_url+"sendotp";
  private _payment=this._url.config_url+"payment";
  private _downloadsecurity=this._url.config_url+"downloadsecurity";

  registerUser(name,email,gender,phonenumber,password):Observable<any>{
    let formData: FormData = new FormData(); 
    formData.append('name',name ); 
    formData.append('email',email ); 
    formData.append('gender',gender ); 
    formData.append('phonenumber',phonenumber ); 
    formData.append('password',password ); 
    console.log(formData,"this formadata")
    return this.http.post<any>(this._adduser,formData)
  }
  loginUser(email,password){
    let formData: FormData = new FormData(); 
    formData.append('password',password ); 
    formData.append('email',email ); 
    return this.http.post<any>(this._login,formData)

  }
  payment(id){
    let formData: FormData = new FormData(); 
    formData.append('id',id ); 
    return this.http.post<any>(this._payment,formData)

  }
  sendotp(email){
    let formData: FormData = new FormData(); 
    formData.append('email',email ); 
    return this.http.post<any>(this._sendotp,formData)

  }
  getaudio(audio,id,software){
    let formData: FormData = new FormData(); 
    formData.append('audio',audio);
    formData.append('filename',software); 
    return this.http.post<any>(this._getaudio+"/"+id,formData)
  }
  
  downloadsecurity(audio,id,productkey){
    let formData: FormData = new FormData(); 
    formData.append('audio',audio);
    formData.append('productkey',productkey); 
    return this.http.post<any>(this._downloadsecurity+"/"+id,formData)
  }
  
}
