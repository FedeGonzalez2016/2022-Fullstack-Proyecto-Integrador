from app import app,mysql
from Models.usersModel import *
from flask import Flask, flash, render_template, request, redirect, url_for, session, jsonify
from flask_mysqldb import MySQLdb
import bcrypt



#Creamos el registro
@app.route('/registro', methods=["GET", "POST"])
def registro():
    if request.method == 'GET':
        return render_template("registro.html")
    else:
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        ciudad = request.form['ciudad']
        usuario = request.form['usuario']
        fecha_nac = request.form['fecha_nac']
        correo = request.form['correo']
        password = request.form['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO clientes (nombre,apellido,telefono,ciudad,usuario,fecha_nac,correo,password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(nombre,apellido,telefono,ciudad,usuario,fecha_nac,correo,hash_password,))
        mysql.connection.commit()
        session['nombre'] = nombre
        session['correo'] = correo
        return redirect(url_for("index"))

#Creamos el login
@app.route('/login', methods=["GET", "POST"])
def login():

    #La librería Python Request es un estándar que sirve para realizar solicitudes HTTP cuando se está desarrollando el lado del servidor de una página web.
    #Hacemos la conexion a la base de datos a traves del método "Post" y guardamos lo ingresado en el frontend, en los campos "usuario" y "password" en las variables declaradas para chequearlo mas adelante.
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password'].encode('utf-8')
        
        #Un cursor es un objeto de acceso a datos que se puede utilizar para recorrer el conjunto de filas de una tabla o insertar nuevas filas en una tabla
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM clientes WHERE usuario=%s",(usuario,))
        user = cur.fetchone()
        cur.close()
#Verificamos el metodo post por medio de un if
        if len(user) > 0:
            if bcrypt.hashpw(password, user['password'].encode('utf-8')) == user['password'].encode('utf-8'):
                session['id'] = user['id']
                session['nombre'] = user['nombre']
                session['apellido'] = user['apellido']
                session['tipo_usuario'] = user['tipo_usuario']

                #Si el tipo de usuario es user, redirige hacia la pagina de inicio.
                if session['tipo_usuario'] == 'user':
                    return redirect(url_for("index"))
                #De lo contrario, si el tipo de usuario es admin, redirige hacia el sistema interno.
                elif session['tipo_usuario'] == 'admin':
                    return redirect(url_for("sistema"))
            else:

                #Si no es ninguno de los dos casos anteriores, devuelve al login, e indica que los datos ingresados son incorrectos.
                flash('Los datos son incorrectos')
                return render_template("login.html")
        else:
            #Si el user que se ha ingresado no tiene mas de 0 caracteres de largo(es decir no se ha ingresado valor alguno), devuelve al login, e indica que los datos ingresados son incorrectos.
            flash('Los datos son incorrectos')
            return render_template("login.html")
    else:
        return render_template("login.html")

#Creamos salir para cerrar sesión
@app.route('/salir')
def salir():
    session.clear()
    return redirect(url_for("index"))
