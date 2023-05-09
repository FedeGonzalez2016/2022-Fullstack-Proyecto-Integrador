import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ConsultaComponent } from './consulta/consulta.component';
import { HabitacionesEcommerceComponent } from './habitaciones-ecommerce/habitaciones-ecommerce.component';
import { NuestraHistoriaComponent } from './nuestra-historia/nuestra-historia.component';
import { RegistroComponent } from './registro/registro.component';
import { ServiciosComponent } from './servicios/servicios.component';
import { ReservasComponent } from './vista-interna/reservas/reservas.component';
import { AuthModule } from '../auth/auth.module';
import { SharedModule } from '../shared/shared.module';




@NgModule({
  declarations: [
    ConsultaComponent,
    HabitacionesEcommerceComponent,
    NuestraHistoriaComponent,
    RegistroComponent,
    ServiciosComponent,
    ReservasComponent
  ],
  imports: [
    CommonModule,
    AuthModule,
    SharedModule
  ]
})
export class PagesModule { }
