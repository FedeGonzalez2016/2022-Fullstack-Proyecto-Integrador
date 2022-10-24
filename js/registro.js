const nombre = document.getElementById("nombre")
const apellido = document.getElementById("apellido")
const telefono = document.getElementById("telefono")
const nombreUsuario = document.getElementById("nombre-usuario")
const email = document.getElementById("email")
const repetirEmail = document.getElementById("repetir-email")
const password = document.getElementById("password")
const repetirPassword = document.getElementById("repetir-password")

form.addEventListener("submit",e=>{
    e.preventDefault()
        if (nombre.value.length <2){
            alert("Por favor, ingrese un nombre mas largo")
        }
        if (apellido.value.length <2){
            alert("Por favor, ingrese un apellido válido")
        }
        if (telefono.value.length <10){
            alert("Por favor, ingrese un telefono válido")
        }
        if (nombreUsuario.value.length <6 && nombreUsuario.value.length >20){
            alert("Por favor, ingrese nombre de usuario válido")
        }
})