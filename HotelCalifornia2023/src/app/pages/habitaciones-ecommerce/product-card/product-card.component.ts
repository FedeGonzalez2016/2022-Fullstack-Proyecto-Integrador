import { Component, OnInit } from '@angular/core';
//import { Reserva } from '../../../interface/reserva.interface';
import { Reserva } from '../../../models/reserva';

@Component({
  selector: 'app-product-card',
  templateUrl: './product-card.component.html',
  styleUrls: ['./product-card.component.css']
})
export class ProductCardComponent implements OnInit {
  public misReservas:Array<Reserva>;

  constructor() { 
    this.misReservas =[
      new Reserva (`Habitación Single o Doble`, `Equipados con microondas, pava eléctrica y heladera tipo frigobar, ideales para prepararse una merienda o un snack (no aptos para comidas más elaboradas). TV-LED. Caja de seguridad en las habitaciones. Conexión a Internet inalámbrica (Wi-Fi).`, [`Baño privado`, `Tv LED`, `Microondas`, `Pava eléctrica`, `frigobar`, `Caja de Seguridad`, `Wi-fi`], true, 3500),
      new Reserva (`Habitación Triple`, `Equipados con cómodos Kitchenette de 2 x 1,8 m. aprox. con microondas, pava eléctrica y heladera tipo frigobar, ideales para prepararse una merienda o un snack (no aptos para comidas más elaboradas). TV-LED. Caja de seguridad en las habitaciones. Conexión a Internet inalámbrica (Wi-Fi). Sommiers de una plaza como camas adicionales.`, [`Baño privado`, `Tv LED`, `Microondas`, `Pava eléctrica`, `frigobar`, `Caja de Seguridad`, `Wi-fi`], true, 3200),
      new Reserva (`Habitación Cuádruple`, `Habitaciones familiares con 2 ambientes, dos camas doble plaza y 1 baño. Algunas con vistas al lago, TV 42 pulgadas con canales internacionales, minibar, etc.`, [`Baño privado`, `Tv LED`, `Microondas`, `Pava eléctrica`, `frigobar`, `Caja de Seguridad`, `Wi-fi`], true, 3000),
      new Reserva (`Suite Exclusiva`, `Amplia y elegante habitación equipada con una cama King, muebles de madera oscura, obras de arte en las paredes, baño privado con artículos de aseo gratuitos, escritorio, frigobar, cafetera,   caja fuerte,  sofá cama y sillón de descanso. Esta habitación cuenta con un balcón privado con sillones y  un gran  jacuzzi   que le garantizan un ambiente ideal para un placentero descanso disfrutando la naturaleza circundante`, [`Baño privado`, `Tv LED`, `Microondas`, `Pava eléctrica`, `frigobar`, `Caja de Seguridad`, `Wi-fi`], true, 5500),
      new Reserva (`Suite Junior Doble`, `Amplia habitación  equipada con dos camas queen. Disponen de muebles de madera oscura, obras de arte en las paredes, baño privado con artículos de aseo gratuitos, escritorio, frigobar,  caja fuerte, cafetera  terraza con sillones para disfrutar de la naturaleza con vista al jardín.`, [`Baño privado`, `Tv LED`, `Microondas`, `Pava eléctrica`, `frigobar`, `Caja de Seguridad`, `Wi-fi`], true, 5000)
    ]
  }

  ngOnInit(): void {
  }

}