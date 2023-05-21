import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ConsultaComponent } from './consulta/consulta.component';
import { HabitacionesEcommerceComponent } from './habitaciones-ecommerce/habitaciones-ecommerce.component';
import { NuestraHistoriaComponent } from './nuestra-historia/nuestra-historia.component';
import { RegistroComponent } from './registro/registro.component';
import { ServiciosComponent } from './servicios/servicios.component';
import { ReservasComponent } from './vista-interna/reservas/reservas.component';
import { RouterModule } from '@angular/router';
import { ProductCardComponent } from './habitaciones-ecommerce/product-card/product-card.component';
import { HttpClientModule } from '@angular/common/http';
import { ReactiveFormsModule, FormsModule} from '@angular/forms'



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
