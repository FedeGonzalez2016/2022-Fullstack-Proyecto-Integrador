var nombre = document.getElementById("nombre")
var apellido = document.getElementById("apellido")
var telefono = document.getElementById("telefono")
var ciudad = document.getElementById("ciudad")
var nombreUsuario = document.getElementById("nombre-usuario")
var email = document.getElementById("email")
var repetirEmail = document.getElementById("repetir-email")
var password = document.getElementById("password")
var repetirPassword = document.getElementById("repetir-password") 

var nombreIncorrecto = document.getElementById("nombre-incorrecto")
var apellidoIncorrecto = document.getElementById("apellido-incorrecto")
var telefonoIncorrecto = document.getElementById("telefono-incorrecto")
var ciudadIncorrecto = document.getElementById("ciudad-incorrecto")
var nombreUsuarioIncorrecto = document.getElementById("nombre-usuario-incorrecto")
var emailIncorrecto = document.getElementById("email-incorrecto")
var repetirEmailIncorrecto = document.getElementById("repetir-email-incorrecto")
var passwordIncorrecto = document.getElementById("password-incorrecto")
var repetirPasswordIncorrecto = document.getElementById("repetir-password-incorrecto")  

var nombreSinIngresar = document.getElementById("nombre-sin-ingresar")
var apellidoSinIngresar = document.getElementById("apellidosin-ingresar")
var telefonoSinIngresar = document.getElementById("telefonosin-ingresar")
var ciudadSinIngresar = document.getElementById("ciudadsin-ingresar")
var nombreUsuarioSinIngresar = document.getElementById("nombre-usuariosin-ingresar")
var emailSinIngresar = document.getElementById("emailsin-ingresar")
var repetirEmailSinIngresar = document.getElementById("repetir-emailsin-ingresar")
var passwordSinIngresar = document.getElementById("passwordsin-ingresar")
var repetirPasswordSinIngresar = document.getElementById("repetir-passwordsin-ingresar") 

form.addEventListener("submit",e=>{
    e.preventDefault()
}
)

function verificarNombre (){
    if (nombre.value == ""){
        //alert("Por favor, ingrese un nombre")
        nombreIncorrecto.style.display="block";
    }else {
        if (nombre.value.length <2){
            // Ingresar un nombre de m??s de una letra, ya que los nombres m??s cortos generalmente poseen m??nimo 2 letras. Con esta verificaci??n, validamos que el campo no este vac??o y que tenga el m??nimo de caracteres necesarios al mismo tiempo.
            // alert("Por favor, ingrese un nombre m??s largo")
            nombreSinIngresar.style.display="block";
        }
    }
}
function ocultarErrorNombre(){
    nombreIncorrecto.style.display="none";
}

function verificarApellido (){
    if (apellido.value == ""){
        //alert("Por favor, ingrese un apellido")
        apellidoIncorrecto.style.display="block";
    }else {
        if (apellido.value.length <2){
            // Ingresar un nombre de m??s de una letra, ya que los nombres m??s cortos generalmente poseen m??nimo 2 letras. Con esta verificaci??n, validamos que el campo no este vac??o y que tenga el m??nimo de caracteres necesarios al mismo tiempo.
            //alert("Por favor, ingrese un apellido m??s largo")
        }
    }
}
function ocultarErrorApellido(){
    apellidoIncorrecto.style.display="none";
}

function verificarTelefono (){
    if (telefono.value == ""){
        //alert("Por favor, ingrese un telefono")
        telefonoIncorrecto.style.display="block";
    }else {
        if (telefono.value.length <10){
            // Por defecto los numeros telefonicos de Argentina (Con caracteristica incluida) rondan los 10 caracteres. Con esta verificaci??n, validamos que el campo no este vac??o y que tenga el m??nimo de caracteres necesarios al mismo tiempo.
            //alert("El n??mero telef??nico ingresado no es correcto")
        }
    }
}
function ocultarErrorTelefono(){
    telefonoIncorrecto.style.display="none";
}

function verificarCiudad (){
    if (ciudad.value == ""){
        //alert("Por favor, ingrese una ubicaci??n")
        ciudadIncorrecto.style.display="block";
    }
}
function ocultarErrorCiudad(){
    ciudadIncorrecto.style.display="none";
}

function verificarUsuario (){
    if (nombreUsuario.value == ""){
        //alert("Por favor, ingrese un usuario")
        nombreUsuarioIncorrecto.style.display="block";
    }else{
        if (nombreUsuario.value.length <6){
            // Validaci??n que establece para nick de usuario un n??mero m??nimo y m??ximo de caracteres.
            //alert("Por favor, ingrese nombre de usuario con 6 caracteres m??nimo y 20 caracteres m??ximo")
        }
    }
}
function ocultarErrorUsuario (){
    nombreUsuarioIncorrecto.style.display="none";
}


function verificarEmail(){
    // Obtenemos los datos a evaluar
    email = document.getElementById("email");
    
    // Validaci??n con Regex (Expresiones regulares; que reemplazan muchos condicionales.)
    // Para consultar documentaci??n verificar el siguiente link "https://www.coderbox.net/blog/validar-email-usando-javascript-y-expresiones-regulares/".
    var emailValido =  /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/;

    // Verificar patr??n de coincidencia de texto
    if( emailValido.test(email.value) ){
        console.log ("Email valido, siga con la suscripci??n")
    }else{
        //alert("Email inv??lido, por favor vuelva a intentarlo");
        emailIncorrecto.style.display="block";
        return false;
    }
}
function ocultarErrorEmail(){
    emailIncorrecto.style.display="none";
}

function verificarEmailRepetido (){
    if (email.value != repetirEmail.value){
        // Validaci??n que verifica que los datos ingresados en los campos "Email" y "Repetir-Email" sean iguales".
        //alert("El email no coincide en los dos campos solicitados")
        repetirEmailIncorrecto.style.display="block";
    }
}
function ocultarErrorEmailRepetido(){
    repetirEmailIncorrecto.style.display="none";
}

function verificarPassword (){
    if (password.value == ""){
        //alert("Por favor, ingrese una contrase??a")
        passwordIncorrecto.style.display="block";
    }else{
        if (password.value.length <6){
            // Validaci??n que establece para contrase??a un n??mero m??nimo y m??ximo de caracteres.
            //alert("Por favor, ingrese contrase??a con 6 caracteres m??nimo y 20 caracteres m??ximo")
        }
    }
}
function ocultarErrorPassword(){
    passwordIncorrecto.style.display="none";
}

function verificarPasswordRepetido (){
    if (password.value != repetirPassword.value){
        // Validaci??n que verifica que los datos ingresados en los campos "Contrase??a" y "Repetir-Contrase??a" sean iguales".
        //alert("La contrase??a no coincide en los dos campos solicitados")
        repetirPasswordIncorrecto.style.display="block";
    }
}
function ocultarErrorPasswordRepetido(){
    repetirPasswordIncorrecto.style.display="none";
}

/*function permitirSoloAlfabeto(event) {
    var charCode = event.keyCode;
   
    if ((charCode > 64 && charCode < 91) || (charCode > 96 && charCode < 123))
      
      return true;
    else
      return false;
  }


  <script>
      document.addEventListener('keydown', (event) => {
            var keyValue = event.key;
            var codeValue = event.code;
          
            console.log("keyValue: " + keyValue);
            console.log("codeValue: " + codeValue);
          }, false);
    </script>
*/

function soloLetras(event){

    key = event.KeyCode || event.which;
    tecla = String.fromCharCode(key).toString();
    letras = "ABCDEFGHIJKLMN??OPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz????????????????????";

    especiales = [8,13];
    tecla_especial = false;
    for (var i in especiales){
        if (key == especiales[i]){
            tecla_especial = true;
            break;
        }
    }

    if (letras.indexOf(tecla) == -1 && !tecla_especial)
    {
     console.log("Ingresar solo letras");
     return false;    

    }

}

function soloNumeros (event){

if (window.event){
   keynum = event.KeyCode; 
}
else{
   keynum = event.which;
}

if (keynum >47 && keynum <58 || keynum == 8 || keynum == 13)
{
    return true;
}else{
    console.log("Ingresar solo numeros");
    return false;
}
}

