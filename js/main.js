
var botonLogin = document.getElementById("botonLogin");

botonLogin.addEventListener("click", login);

//prueba de botones, no finalizado

function login() {
    var user, pass;
    //var logged =false;

    user = document.getElementById('floatingInput').value;
    pass = document.getElementById('floatingPassword').value;


    if(user == "user1" && pass == "1234"){
        window.location = "../index.html";
        //logged=true; 
    }

    // if logged {
    //     funcion para mostrar los elementos "logueados"
    //     funcion para "ocultar" los links a "registrate" y "login"
    // }
   
}


    // function mostrarLogueado() {
        
    //     if(window.location ="../index.html"){    
    //         document.getElementById('logueado').style.display ="block"

    //     }
    // }

