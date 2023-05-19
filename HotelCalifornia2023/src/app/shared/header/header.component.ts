import { Component, OnInit } from '@angular/core';
import { LoginService } from 'src/app/services/login.service';
import { User } from 'src/app/services/user';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  userLoginOn:boolean=false;
  userData?:User;
  constructor(private loginService:LoginService) { }

  ngOnInit(): void {
    this.loginService.currentUserLoginOn.subscribe({
      next:(userLoginOn)=> {
        this.userLoginOn=userLoginOn;
      }
    });
    this.loginService.currentUserData.subscribe({
      next:(userData)=>{
      this.userData=userData;
      }
    })
  }

}
