
var botonLogin = document.getElementById("botonLogin");

botonLogin.addEventListener("click", login);

//prueba de botones, no finalizado

function login() {
    var user, pass;

    user = document.getElementById('floatingInput').value;
    pass = document.getElementById('floatingPassword').value;


    if(user == "user1" && pass == "1234"){
        window.location = "../index.html";

    }
   
}


    // function mostrarLogueado() {
        
    //     if(window.location ="../index.html"){    
    //         document.getElementById('logueado').style.display ="block"

    //     }
    // }

