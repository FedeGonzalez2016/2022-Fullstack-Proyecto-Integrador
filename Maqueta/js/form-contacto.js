var contactoNombre = document.getElementById("contactoNombre")
var contactoEmail = document.getElementById("contactoEmail")

form.addEventListener("submit",e=>{
    e.preventDefault()
}
)

function verificarEmail(){
    // Obtenemos los datos a evaluar
    contactoEmail = document.getElementById("contactoEmail");
    
    // Validación con Regex (Expresiones regulares; que reemplazan muchos condicionales.)
    // Para consultar documentación verificar el siguiente link "https://www.coderbox.net/blog/validar-email-usando-javascript-y-expresiones-regulares/".
    var emailValido =  /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/;

    // Verificar patrón de coincidencia de texto
    if( emailValido.test(email.value) ){
        console.log ("Email valido, siga con la suscripción")
    }else{
        //alert("Email inválido, por favor vuelva a intentarlo");
        emailIncorrecto.style.display="block";
        return false;
    }
}

function verificarNombre (){
    if (nombre.value == ""){
        //alert("Por favor, ingrese un nombre")
        nombreIncorrecto.style.display="block";
    }else {
        if (nombre.value.length <2){
            // Ingresar un nombre de más de una letra, ya que los nombres más cortos generalmente poseen mìnimo 2 letras. Con esta verificación, validamos que el campo no este vacío y que tenga el mínimo de caracteres necesarios al mismo tiempo.
            // alert("Por favor, ingrese un nombre más largo")
            nombreSinIngresar.style.display="block";
        }
    }
}

 function soloLetras(event){

    key = event.KeyCode || event.which;
    tecla = String.fromCharCode(key).toLowerCase();
    letras = "abcdefghijklmnopqrstuvwxyzÁÉÍÓÚáéíóú";

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

