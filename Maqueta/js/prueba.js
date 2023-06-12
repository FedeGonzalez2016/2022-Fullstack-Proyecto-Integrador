var logueadoCerrar = document.getElementById("logueadoCerrar")
var logueadoBienvenido = document.getElementById("logueadoBienvenido")
var logueadoReserva = document.getElementById("logueadoReserva")
var deslogLogin = document.getElementById("deslogLogin")
var deslogRegistrate = document.getElementById("deslogRegistrate")

var logueado = true

document.body.onload = function() {
    if (logueado){
        logueadoCerrar.style.display="block";
        logueadoBienvenido.style.display="block";
        logueadoReserva.style.display="block";
        deslogLogin.style.display="none";
        deslogRegistrate.style.display="none";
    }

        }

logueadoCerrar.addEventListener('click', logOut);

function logOut() {
        alert('¿Desea cerrar sesión?');
        logueadoCerrar.style.display="none";
        logueadoBienvenido.style.display="none";
        logueadoReserva.style.display="none";
        deslogLogin.style.display="block";
        deslogRegistrate.style.display="block";
        

}

