import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

interface Consulta {
  id: string;
  fecha: string;
  nombre: string;
  email: string;
  mensaje: string;
}

@Injectable({
  providedIn: 'root'
})
export class ConsultaService {

  private apiConsultas: string = "http://localhost:3000/consultas";

  constructor(private http: HttpClient) { }

  realizarConsulta(nombre: string, email: string, mensaje: string): Observable<Consulta> {
    const consulta: Consulta = {
      id: Date.now().toString(),
      fecha: new Date().toISOString(),
      nombre: nombre,
      email: email,
      mensaje: mensaje
    };
    return this.http.post<Consulta>(`${this.apiConsultas}`, consulta);
  }


}

