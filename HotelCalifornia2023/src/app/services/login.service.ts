import { Injectable } from '@angular/core';
import { LoginRequest } from './loginRequest';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject, tap } from 'rxjs';
import { User } from './user';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  currentUserLoginOn : BehaviorSubject<boolean> = new BehaviorSubject<boolean>(false);
  currentUserData : BehaviorSubject<User> = new BehaviorSubject<User>({clienteId:0, email:''});

  constructor(private http: HttpClient) {}

  login(_credentials:LoginRequest):Observable<User>{
    return this.http.get<User>('././assets/clientes.json').pipe(
      tap(userData => {
        this.currentUserData.next(userData);
        this.currentUserLoginOn.next(true);
      })
    )
  }



  get userData():Observable<User>{
  return this.currentUserData.asObservable();

  }
 
  get userLoginOn():Observable<boolean>{
  return this.currentUserLoginOn.asObservable();

  }

}