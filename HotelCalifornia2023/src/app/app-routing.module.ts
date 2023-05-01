import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HabitacionesEcommerceComponent } from './pages/habitaciones-ecommerce/habitaciones-ecommerce.component';
import { NuestraHistoriaComponent } from './pages/nuestra-historia/nuestra-historia.component';

const routes: Routes = [
  {path:'habitaciones', component: HabitacionesEcommerceComponent},
  {path:'nuestra-historia', component: NuestraHistoriaComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }