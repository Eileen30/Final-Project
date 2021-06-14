import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CreditcarddetailsComponent } from './creditcarddetails/creditcarddetails.component';
import { DownloadComponent } from './download/download.component';
import { FileselectComponent } from './fileselect/fileselect.component';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { OtpgenerationComponent } from './otpgeneration/otpgeneration.component';
import { PayamountComponent } from './payamount/payamount.component';
import { RegisterComponent } from './register/register.component';
import { WelcomeComponent } from './welcome/welcome.component';

const routes: Routes = [
  { path: '', component: WelcomeComponent},
  { path: 'register', component: RegisterComponent},
  { path: 'login', component: LoginComponent},
  { path: 'home', component: HomeComponent},
  { path: 'download', component: DownloadComponent},
  { path: 'fileselect', component: FileselectComponent},
  { path: 'payamount', component: PayamountComponent},
  { path: 'creditcard', component: CreditcarddetailsComponent},
  { path: 'otpgenerate', component: OtpgenerationComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
