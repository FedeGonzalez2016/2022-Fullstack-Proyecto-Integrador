import { Component, OnInit } from '@angular/core';
import { FacturaService } from 'src/app/services/factura.service';
import { Factura } from 'src/app/services/factura';

@Component({
  selector: 'app-reservas',
  templateUrl: './reservas.component.html',
  styleUrls: ['./reservas.component.css']
})
export class ReservasComponent implements OnInit {
  constructor( private facturaService: FacturaService) { }
  factura: any;

   ngOnInit(): void {
     this.facturaService.Factura().subscribe((Factura) => {
      console.log(Factura);
     });
     this.facturaService.detalle().subscribe((detalle) => {
      console.log(detalle);
     });
     this.facturaService.detallePago().subscribe((detallePago) => {
      console.log(detallePago);
     });
    }


     addFactura(){
      this.facturaService.addFactura(this.factura).subscribe((factura) => {
        console.log('factura'+ this.addFactura);
      })
     }

     addDetalle(){
      this.facturaService.addDetalle(this.factura).subscribe((detalle) => {
        console.log('detalle' + this.addDetalle)
      })
     }
     addDetallePago(){
      this.facturaService.addFactura(this.factura).subscribe((detallePago) => {
        console.log('detallePago'+ this.addDetallePago);
      })
     }
     addTipoPago(){
      this.facturaService.addFactura(this.factura).subscribe((tipoPago) => {
        console.log('detallePago'+ this.addTipoPago);
      })
     }
    }
