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

#Creacion de crud clientes

#INSERT

@app.route('/agregar_cliente', methods=['POST'])
def agregar_cliente():
    cur = mysql.connection.cursor()
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    telefono = request.form['telefono']
    ciudad = request.form['ciudad']
    usuario = request.form['usuario']
    fecha_nac = request.form['fecha_nac']
    correo = request.form['correo']
    password = request.form['password'].encode('utf-8')
    hash_password = bcrypt.hashpw(password, bcrypt.gensalt())
    cur.execute("INSERT INTO clientes (nombre, apellido, telefono, ciudad, usuario, fecha_nac, correo, password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(nombre, apellido, telefono, ciudad, usuario, fecha_nac, correo,hash_password))
    mysql.connection.commit()
    flash('Usuario agregado correctamente')
    return redirect('/clientes')


#SELECT/LEER

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

#EDIT/ACTUALIZAR

@app.route('/actualizar_cliente', methods=['POST'])
def actualizar_cliente():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        id_data = request.form['id']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        telefono = request.form['telefono']
        fecha_nac = request.form['fecha_nac']
        ciudad = request.form['ciudad']
        cur.execute("UPDATE clientes SET nombre = %s, apellido = %s, correo = %s, telefono = %s, fecha_nac = %s,  ciudad = %s WHERE id=%s",(nombre,apellido,correo,telefono,fecha_nac,ciudad,id_data))
        mysql.connection.commit()
        return redirect('/clientes')

#DELETE

@app.route('/eliminar/<string:id_data>', methods=['GET'])
def eliminar(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM clientes WHERE id=%s",(id_data,))
    mysql.connection.commit()
    flash('Usuario eliminado correctamente')
    return redirect('/clientes')



#Creacion de Crud instalaciones
#Insertar datos
@app.route('/agregar_instalaciones', methods=['POST'])
def agregar_instalaciones():
    cur = mysql.connection.cursor()
    habitacion = request.form['habitacion']
    estado = request.form['estado']
    id_cliente = request.form['id_cliente']
    tipo = request.form['tipo']
    piso = request.form['piso']
    cur.execute("INSERT INTO instalaciones (habitacion,estado,id_cliente,tipo,piso) VALUES(%s,%s,%s,%s,%s)",(habitacion,estado,id_cliente,tipo,piso,))
    mysql.connection.commit()
    flash('Usuario agregado correctamente')
    return redirect('/instalaciones')
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
@app.route('/actualizar_instalaciones', methods=['POST'])
def actualizar_instalaciones():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        habitacion = request.form['habitacion']
        estado = request.form['estado']
        id_cliente = request.form['id_cliente']
        tipo = request.form['tipo']
        piso = request.form['piso']
        cur.execute("UPDATE instalaciones SET habitacion = %s, estado = %s, id_cliente = %s, tipo = %s, piso = %s WHERE id=%s",(habitacion,estado,id_cliente,tipo,piso))
        mysql.connection.commit()
        return redirect('/instalaciones')
#Eliminar datos
@app.route('/eliminar/<string:id_data>', methods=['GET'])
def eliminarf(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM instalaciones WHERE id=%s",(id_data))
    mysql.connection.commit()
    flash('Usuario eliminado correctamente')
    return redirect('/instalaciones')

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
