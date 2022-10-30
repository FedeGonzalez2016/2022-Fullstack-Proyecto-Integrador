/*
var btn = document.getElementById('btn');
var password = document.getElementById('password');
var password_incorrecto = document.getElementById('password-incorrecto');
var usuario = document.getElementById('usuario');
var mensaje_para_no_usuario = document.getElementById('mensaje-para-no-usuario');

/*en tu login te falto agregarle un id a tu botón y pasarle tu funcion validar2(), 
yo lo hago con listeners para no poner funciones js en el HTML, buenas prácticas, 
valido que no vengan vacios los campos y agrego la funcion de evt.preventDefault() 
como su nombre lo indica previene o cancela el evento si es que fuera cancelable en este caso 
el submit lo es y retorno un false para que no siga ejecutando la estructura del if*/


function login(){
    var user,pass;

    user = document.getElementById("floatingInput").value;
    pass = document.getElementById("floatingPassword").value;

    if(user == "alejandro" && pass == "mainero"){
        window.location = "/index.html";
    else 
        alert("Nombre de usuario y/o contraseña incorrecto")
    
    }
}

/*
btn.addEventListener('click', function(evt){
    if(password.value === ''){
        console.log('No olvides rellenar el campo contraseña!')
        alert('No olvides rellenar el campo contraseña!')
        evt.preventDefault();
        return false;
    }
    
    else if(usuario.value === ''){
        console.log('No olvides rellenar el campo usuario!')
        alert('No olvides rellenar el campo de usuario!')
        evt.preventDefault();
        return false;
    }
    else if(usuario.value.length > 30){
        console.log('El nombre del usuario es demasiado largo!')
        alert('El nombre del usuario es demasiado largo')
        evt.preventDefault();
        return false;
    }
});