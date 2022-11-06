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
