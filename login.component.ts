import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthserviceService } from '../authservice.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  email;
  password;

  constructor(private auth: AuthserviceService, private router: Router) { }

  ngOnInit(): void {
  }
  loginUser() {
    this.auth.loginUser(this.email,this.password).subscribe((res) => {
      if (res.token != undefined) {
        console.log(res.token + "this is token");
        localStorage.setItem("access_token", res.token);
        localStorage.setItem("email", res.email);
        localStorage.setItem("id", res.id);
        localStorage.setItem("name", res.name);
        localStorage.setItem("role", res.role);
        this.router.navigate(["/fileselect", { id: res.id, email: res.email }]);
      } else {
        alert("invalid email or password");
      }
    });
  }

}
