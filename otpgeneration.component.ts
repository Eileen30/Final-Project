import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthserviceService } from '../authservice.service';
import { FileserviceService } from '../fileservice.service';

@Component({
  selector: 'app-otpgeneration',
  templateUrl: './otpgeneration.component.html',
  styleUrls: ['./otpgeneration.component.scss']
})
export class OtpgenerationComponent implements OnInit {
  id;
 otp;
  constructor(private otpser: FileserviceService,private mys: AuthserviceService,private router: Router) { }

  ngOnInit(): void {
    this.id=localStorage.getItem('id')
  }
  payment(){
    console.log(this.otp)
    console.log(this.otpser.otp)
    if(this.otp==this.otpser.otp){
      this.mys.payment(this.id)
    .subscribe(
      res =>
      {
          console.log(res)
  
      });
      alert("Payment Completed Successfully")
     //this.router.navigate(["/download"])
  }
    }
    download()
    {   
      this.router.navigate(["/download"])
    }
  }


