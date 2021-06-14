import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RegisterComponent } from './register/register.component';
import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { DownloadComponent } from './download/download.component';
import { FileselectComponent } from './fileselect/fileselect.component';
import { PayamountComponent } from './payamount/payamount.component';
import { CreditcarddetailsComponent } from './creditcarddetails/creditcarddetails.component';
import { OtpgenerationComponent } from './otpgeneration/otpgeneration.component';


@NgModule({
  declarations: [
    AppComponent,
    RegisterComponent,
    LoginComponent,
    HomeComponent,
    WelcomeComponent,
    DownloadComponent,
    FileselectComponent,
    PayamountComponent,
    CreditcarddetailsComponent,
    OtpgenerationComponent,
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
