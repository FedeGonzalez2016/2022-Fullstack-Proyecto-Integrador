import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HabitacionesEcommerceComponent } from './pages/habitaciones-ecommerce/habitaciones-ecommerce.component';
import { LoginComponent } from './auth/login/login.component';
import { RegistroComponent } from './pages/registro/registro.component';
import { ConsultaComponent } from './pages/consulta/consulta.component';

@NgModule({
  declarations: [
    AppComponent,
    HabitacionesEcommerceComponent,
    LoginComponent,
    RegistroComponent,
    ConsultaComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
