import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthserviceService } from '../authservice.service';
import { FileserviceService } from '../fileservice.service';

@Component({
  selector: 'app-creditcarddetails',
  templateUrl: './creditcarddetails.component.html',
  styleUrls: ['./creditcarddetails.component.scss']
})
export class CreditcarddetailsComponent implements OnInit {
 email;
 otp;
  constructor(private router: Router,private mys: AuthserviceService,private otpser: FileserviceService) { }

  ngOnInit(): void {
    this.email=localStorage.getItem('email')
  }
  gotopage(){
    this.mys.sendotp(this.email)
    .subscribe(
      res =>
      {
          console.log(res)
          this.otpser.otp=res.otp;
      });
    this.router.navigate(["/otpgenerate"])
  }

}
