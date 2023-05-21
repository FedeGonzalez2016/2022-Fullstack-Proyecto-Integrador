import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HabitacionesEcommerceComponent } from './pages/habitaciones-ecommerce/habitaciones-ecommerce.component';
import { NuestraHistoriaComponent } from './pages/nuestra-historia/nuestra-historia.component';
import { ConsultaComponent } from './pages/consulta/consulta.component';
import { LoginComponent } from './auth/login/login.component';
import { RegistroComponent } from './pages/registro/registro.component';
import { ServiciosComponent } from './pages/servicios/servicios.component';

const routes: Routes = [
  {path:'', redirectTo:'/nosotros', pathMatch:'full'},
  {path:'habitaciones', component: HabitacionesEcommerceComponent},
  {path:'nosotros', component: NuestraHistoriaComponent},
  {path:'consulta', component: ConsultaComponent},
  {path:'login', component: LoginComponent},
  {path:'registro', component: RegistroComponent},
  {path:'servicios', component: ServiciosComponent},
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
