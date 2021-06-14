import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthserviceService } from '../authservice.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  name;
  email;
  phonenumber;
  gender;
  password;
  confirm_password;
  constructor(private reg: AuthserviceService, private router: Router) { }

  ngOnInit(): void {
  }
  registerUser(value : any)
  {
    this.reg.registerUser(this.name,this.email,this.gender,this.phonenumber,this.password)
    .subscribe(
      res =>
      {
        alert("Registered Successfully");
        this.router.navigate(['/login'])
      },
      err=>console.log("mmm"+err)
    )
  }

}
