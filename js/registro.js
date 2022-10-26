var nombre = document.getElementById("nombre")
var apellido = document.getElementById("apellido")
var telefono = document.getElementById("telefono")
var ciudad = document.getElementById("ciudad")
var nombreUsuario = document.getElementById("nombreUsuario")
var email = document.getElementById("email")
var repetirEmail = document.getElementById("repetir-email")
var password = document.getElementById("password")
var repetirPassword = document.getElementById("repetirPassword")          

form.addEventListener("submit",e=>{
    e.preventDefault()
}
)

function verificarNombre (){
    if (nombre.value == ""){
        alert("Por favor, ingrese un nombre")
    }else {
        if (nombre.value.length <2){
            // Ingresar un nombre de más de una letra, ya que los nombres más cortos generalmente poseen mìnimo 2 letras. Con esta verificación, validamos que el campo no este vacío y que tenga el mínimo de caracteres necesarios al mismo tiempo.
            alert("Por favor, ingrese un nombre más largo")
        }
    }
}

function verificarApellido (){
    if (apellido.value == ""){
        alert("Por favor, ingrese un apellido")
    }else {
        if (apellido.value.length <2){
            // Ingresar un nombre de más de una letra, ya que los nombres más cortos generalmente poseen mìnimo 2 letras. Con esta verificación, validamos que el campo no este vacío y que tenga el mínimo de caracteres necesarios al mismo tiempo.
            alert("Por favor, ingrese un apellido más largo")
        }
    }
}

function verificarTelefono (){
    if (telefono.value == ""){
        alert("Por favor, ingrese un telefono")
    }else {
        if (telefono.value.length <10){
            // Por defecto los numeros telefonicos de Argentina (Con caracteristica incluida) rondan los 10 caracteres. Con esta verificación, validamos que el campo no este vacío y que tenga el mínimo de caracteres necesarios al mismo tiempo.
            alert("El número telefónico ingresado no es correcto")
        }
    }
}
// Esta función impide que ingresemos caracteres que no esten comprendidos entre el codigo 48 y 57 (numeros) de la codificacion ASCII
function valideKey(evt){
    
    // code is the decimal ASCII representation of the pressed key.
    var code = (evt.which) ? evt.which : evt.keyCode;
    
    if(code==8) { // backspace.
      return true;
    } else if(code>=48 && code<=57) { // is a number.
      return true;
    } else{ // other keys.
      return false;
    }
}

function verificarCiudad (){
    if (ciudad.value == ""){
        alert("Por favor, ingrese una ubicación")
    }
}

function verificarUsuario (){
    if (nombreUsuario.value == ""){
        alert("Por favor, ingrese un usuario")
    }else{
        if (nombreUsuario.value.length <6){
            // Validación que establece para nick de usuario un número mínimo y máximo de caracteres.
            alert("Por favor, ingrese nombre de usuario con 6 caracteres mínimo y 20 caracteres máximo")
        }
    }
}


function verificarEmail(){
    // Obtenemos los datos a evaluar
    email = document.getElementById("email");
    
    // Validación con Regex (Expresiones regulares; que reemplazan muchos condicionales.)
    // Para consultar documentación verificar el siguiente link "https://www.coderbox.net/blog/validar-email-usando-javascript-y-expresiones-regulares/".
    var emailValido =  /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/;

    // Verificar patrón de coincidencia de texto
    if( emailValido.test(email.value) ){
        console.log ("Email valido, siga con la suscripción")
    }else{
        alert("Email inválido, por favor vuelva a intentarlo");
        return false;
    }
}

function verificarEmailRepetido (){
    if (email.value != repetirEmail.value){
        // Validación que verifica que los datos ingresados en los campos "Email" y "Repetir-Email" sean iguales".
        alert("El email no coincide en los dos campos solicitados")
    }
}

function verificarPassword (){
    if (password.value == ""){
        alert("Por favor, ingrese una contraseña")
    }else{
        if (password.value.length <6){
            // Validación que establece para contraseña un número mínimo y máximo de caracteres.
            alert("Por favor, ingrese contraseña con 6 caracteres mínimo y 20 caracteres máximo")
        }
    }
}

function verificarPasswordRepetido (){
    if (password.value != repetirPassword.value){
        // Validación que verifica que los datos ingresados en los campos "Contraseña" y "Repetir-Contraseña" sean iguales".
        alert("La contraseña no coincide en los dos campos solicitados")
    }
}








