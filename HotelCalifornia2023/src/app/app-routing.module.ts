import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HabitacionesEcommerceComponent } from './pages/habitaciones-ecommerce/habitaciones-ecommerce.component';
import { NuestraHistoriaComponent } from './pages/nuestra-historia/nuestra-historia.component';
import { ConsultaComponent } from './pages/consulta/consulta.component';
import { LoginComponent } from './auth/login/login.component';
import { RegistroComponent } from './pages/registro/registro.component';

const routes: Routes = [
  {path:'habitaciones', component: HabitacionesEcommerceComponent},
  {path:'nuestra-historia', component: NuestraHistoriaComponent},
  {path:'consulta', component: ConsultaComponent},
  {path:'login', component: LoginComponent},
  {path:'registro', component: RegistroComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }