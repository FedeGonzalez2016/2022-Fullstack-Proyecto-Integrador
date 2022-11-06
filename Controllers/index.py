from app import app
from flask import Flask, flash, render_template, request, redirect, url_for, session, jsonify

#Creamos la ruta index
@app.route('/')
def index():
    return render_template('index.html')
    
#Creamos la ruta consulta
@app.route('/consulta')
def consulta():
    return render_template('contact2.html')
