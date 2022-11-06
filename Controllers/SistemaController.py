from app import app,mysql
from flask import Flask, flash, render_template, request, redirect, url_for, session, jsonify
from flask_mysqldb import MySQLdb
import bcrypt
#Ruta sistema
@app.route('/sistema')
def sistema():
    cur = mysql.connection.cursor()
    cur.execute("SELECT COUNT(*)")
    data = cur.fetchall()
    return render_template("sistema/inicio.html", datos=data)

#Creacion de Crud Clientes

#Insertar datos

#Leer los datos
#Ruta clientes
@app.route('/clientes')
def clientes():
    if session['tipo_usuario'] == 'admin':
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM clientes")
        data = cur.fetchall()
        cur.close()
        return render_template("sistema/cliente.html", clientes=data)
    else:
        return redirect(url_for("index"))

#Editar los datos

#Eliminar datos


#Creacion de Crud instalaciones
#Insertar datos

#Leer los datos
#Ruta instalaciones
@app.route('/instalaciones')
def instalaciones():
    if session['tipo_usuario'] == 'admin':
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM instalaciones")
        data = cur.fetchall()
        cur.close()
        return render_template("sistema/instalaciones.html", instalaciones=data)
    else:
        return redirect(url_for("index"))

#Editar los datos

#Eliminar datos


#Creacion de Crud reservas
#Insertar datos

#Leer los datos
#Ruta reservas
@app.route('/reservas')
def reservas():
    if session['tipo_usuario'] == 'admin':
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM reservas")
        data = cur.fetchall()
        cur.close()
        return render_template("sistema/reservas.html", reservas=data)
    else:
        return redirect(url_for("index"))

#Editar los datos

#Eliminar datos