// Example starter JavaScript for disabling form submissions if there are invalid fields

(() => {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.formulario')

    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault()
                event.stopPropagation()
            }

        form.classList.add('non-validated')
        }, false)
    })
    })() 




function onEnviar(){
    let form = document.getElementById("myform");
    let user = document.forms["myform"]["nombreUsuario"].value;
    let password = document.forms["myform"]["floatingPassword"].value;
    document.getElementById("usuario-sin-ingresar").style.display = "none";
    document.getElementById("usuario-incorrecto").style.display = "none";
    document.getElementById("contrasena-sin-ingresar").style.display = "none";
    document.getElementById("contrasena-incorrecta").style.display = "none"
    
    
    if (form.checkValidity() && user == "user1" && password == "123"){
        
                
        window.location = '../index.html'; 
        
        
        alert("Pasó la validación correctamente. Llamar a controlador."); 
        }
    
    if (user == ""){
        console.log("Usuario vacío")
        document.getElementById("usuario-sin-ingresar").style.display = "block";
        event.preventDefault();
        event.stopPropagation()
    }
    else if(user != "user1"){
        console.log("Usuario incorrecto")
        document.getElementById("usuario-incorrecto").style.display = "block";
        event.preventDefault();
        event.stopPropagation()
    }
    
    if (password == ""){
        console.log("Password vacío")
        document.getElementById("contrasena-sin-ingresar").style.display = "block";
        event.preventDefault();
        event.stopPropagation()
    }
    else if(password != "123"){
        console.log("Contraseña incorrecta")
        document.getElementById("contrasena-incorrecta").style.display = "block";
        event.preventDefault();
        event.stopPropagation()
    }
}
