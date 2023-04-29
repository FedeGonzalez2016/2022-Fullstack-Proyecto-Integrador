import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HabitacionesEcommerceComponent } from './pages/habitaciones-ecommerce/habitaciones-ecommerce.component';

@NgModule({
  declarations: [
    AppComponent,
    HabitacionesEcommerceComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
