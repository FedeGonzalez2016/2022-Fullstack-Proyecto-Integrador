from flask import Flask, flash, render_template, request, redirect, url_for, session, jsonify #Llamamos a Flask | pip install Flask
from flask_mysqldb import MySQL,MySQLdb #Base de datos | pip install Flask-MySQLdb
import bcrypt
from functools import wraps


app = Flask(__name__)
#Conexion a la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ispc'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
app.secret_key = "023jsdjk#4sfdfdgdg"

from Controllers.UsersController import *
from Controllers.index import *
from Controllers.SistemaController import *
if __name__=='__main__':
    app.run(debug=True)