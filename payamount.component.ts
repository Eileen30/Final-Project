import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FileserviceService } from '../fileservice.service';

@Component({
  selector: 'app-payamount',
  templateUrl: './payamount.component.html',
  styleUrls: ['./payamount.component.scss']
})
export class PayamountComponent implements OnInit {
  productkey;

  constructor(private router: Router,private soft: FileserviceService) { }

  ngOnInit(): void {
    this.productkey=this.soft.productkey;
    console.log(this.productkey)
  }
  payment()
  {
    this.router.navigate(["/creditcard"])
  }

}
