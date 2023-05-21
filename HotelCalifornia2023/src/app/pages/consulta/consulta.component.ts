import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { ConsultaService } from 'src/app/services/consulta.service';


@Component({
  selector: 'app-consulta',
  templateUrl: './consulta.component.html',
  styleUrls: ['./consulta.component.css']
})
export class ConsultaComponent implements OnInit {

nombreHotel = 'Hotel California';
infoHotel = 'Descubre nuestro hotel con spa: relajación, tratamientos rejuvenecedores y una experiencia inolvidable. ¡Reserva ahora y déjate consentir! Comunícate con nosotros para más información.';
direccionHotel = 'Calle Falsa 123';
cpHotel = '4250';
ciudadHotel = 'Villa Carlos Paz';
provinciaHotel = 'Córdoba';
paisHotel = 'Argentina';
emailHotel = 'info@hotelcalifornia.com';
telefonoHotel = '03564 - 4315000';
instagramHotel = 'Hotel California';
facebookHotel = 'Hotel California';
twitterHotel = 'Hotel California';

consultaForm: FormGroup;
consultaEnviada: boolean = false;

  constructor(private fb: FormBuilder, private consultaService: ConsultaService) {
    this.consultaForm = this.fb.group({
      nombre: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      mensaje: ['',Validators.required]
    });
    }

  ngOnInit(): void {
  }

  onConsulta(): void {
    if (this.consultaForm.valid){
      console.log("Llamar al servicio de Consulta");
      
      const nombre = this.consultaForm.get('nombre')!.value;
      const email = this.consultaForm.get('email')!.value;
      const mensaje = this.consultaForm.get('mensaje')!.value;

      this.consultaService.realizarConsulta(nombre, email, mensaje).subscribe(
        respuesta => {
          console.log(respuesta);
          this.consultaForm.reset();
          this.consultaEnviada = true;
        },
        error => {
          console.error(error);
        }
      );

    } else {
      this.consultaForm.markAllAsTouched();
    }
  }


    

}

