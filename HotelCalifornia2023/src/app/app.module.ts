import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HabitacionesEcommerceComponent } from './pages/habitaciones-ecommerce/habitaciones-ecommerce.component';
import { LoginComponent } from './auth/login/login.component';
import { RegistroComponent } from './pages/registro/registro.component';
import { ConsultaComponent } from './pages/consulta/consulta.component';
import { HeaderComponent } from './shared/header/header.component';
import { FooterComponent } from './shared/footer/footer.component';
import { ServiciosComponent } from './pages/servicios/servicios.component';

@NgModule({
  declarations: [
    AppComponent,
    HabitacionesEcommerceComponent,
    LoginComponent,
    RegistroComponent,
    ConsultaComponent,
    HeaderComponent,
    FooterComponent,
    ServiciosComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
