import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaderResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { catchError, filter, map, tap } from 'rxjs/operators';
import { Factura, detallePago, tipoPago } from './factura';
@Injectable({
  providedIn: 'root'
})
export class FacturaService {

  constructor( private http : HttpClient) { }
  FacturaUrl= ' http://localhost:3000';
 
 //get 
 Factura(){
  return this.http.get<Factura[]>('././assets/hotel.json').pipe(
    map((fact : any) => fact.factura)
  )
 }
   detalle() {
    return this.http.get<tipoPago[]>('././assets/hotel.json').pipe(
      map((data: any) => data.tipoPago)
    )
  }
  detallePago(): Observable <detallePago[]>{
     return this.http.get<[]>('././assets/hotel.json').pipe(
      map((deta : any) => deta.detalle)
     )

   }
   tipoPago(): Observable <Object>{
   return this.http.get('././assets/hotel.json').pipe(
    map((tip : any) => tip.tipoPago)
    )
    }

//post


   addFactura(factura:Factura): Observable<any>{
    const headers = {'Content-type': 'application/json'}
    const body = JSON.stringify(factura);
    console.log('ingresar datos' + body)
    return this.http.post(this.FacturaUrl+'factura'+ body,{'headers': headers})
    
  }
  addDetalle(detalle: Factura){
    const headers = {'Content-type': 'application/json'}
    const body = JSON.stringify(detalle);
    console.log('ingresar datos' + body)
    return this.http.post(this+'detalles'+ body,{'headers': headers})
  }

  addDetallePg(){
    const headers = {'Content-type': 'application/json'}
    const body = JSON.stringify(this.detallePago);
    console.log('ingresar datos' + body)
    return this.http.post(this+'detallePago'+body,{'headers': headers})
  }

  addTipoPago(){
    const headers = {'Content-type': 'application/json'}
    const body = JSON.stringify(this.tipoPago);
    console.log('ingresar datos' + body)
    return this.http.post(this+'tipoPago'+body,{'headers': headers})
  }
}