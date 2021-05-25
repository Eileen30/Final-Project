import { Component, OnInit, Output } from '@angular/core';
import { Router } from '@angular/router';
import { FileserviceService } from '../fileservice.service';

@Component({
  selector: 'app-fileselect',
  templateUrl: './fileselect.component.html',
  styleUrls: ['./fileselect.component.scss']
})
export class FileselectComponent implements OnInit {
 


software;
  constructor(private router: Router,private soft:FileserviceService) { }

  ngOnInit(): void {
  }
  nextpage(){
    alert(this.software)
    this.soft.software=this.software;
    this.router.navigate(["/home"])
  }

}
