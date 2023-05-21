/* comando para crear servicio: ng g s services/Reserva */
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Reserva } from 'src/app/models/reserva'; // pendiente de creacion

@Injectable({
  providedIn: 'root'
})
export class ReservaService {
  URL= "../../assets/hotelcalifornia.json";
  constructor(private http: HttpClient ) { }


  //estoi no funciona, solo copie el modelo de otro
  public getReserva(): Observable <Reserva>{
    return this.http.get<Reserva>(this.URL + 'traer/nroReserva');

  }
}
