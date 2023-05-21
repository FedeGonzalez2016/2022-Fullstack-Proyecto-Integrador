import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ConsultaComponent } from './consulta/consulta.component';
import { HabitacionesEcommerceComponent } from './habitaciones-ecommerce/habitaciones-ecommerce.component';
import { NuestraHistoriaComponent } from './nuestra-historia/nuestra-historia.component';
import { RegistroComponent } from './registro/registro.component';
import { ServiciosComponent } from './servicios/servicios.component';
import { ReservasComponent } from './vista-interna/reservas/reservas.component';
import { RouterModule } from '@angular/router';
<<<<<<< HEAD
import { HttpClientModule } from '@angular/common/http';
import { ReactiveFormsModule, FormsModule} from '@angular/forms'
=======
import { ProductCardComponent } from './habitaciones-ecommerce/product-card/product-card.component';
>>>>>>> 887f7afcab0df608eb7d3b1266bddc2f3e2b7fae



@NgModule({
  declarations: [
    ConsultaComponent,
    HabitacionesEcommerceComponent,
    NuestraHistoriaComponent,
    RegistroComponent,
    ServiciosComponent,
    ReservasComponent,
    ProductCardComponent
  ],
  imports: [
    CommonModule,
    RouterModule,
    HttpClientModule,
    ReactiveFormsModule,
    FormsModule,
    
    
  ]
})
export class PagesModule { }
