from conexion import conn

class UsersTabla():
    cursor = conn.cursor()
    sql = """CREATE TABLE clientes (id INT AUTO_INCREMENT PRIMARY KEY,nombre VARCHAR(100),apellido VARCHAR(100),telefono INT(12),ciudad VARCHAR(100),usuario VARCHAR(100,fecha_nac DATE,correo VARCHAR(100),password VARCHAR(100),tipo_usuario VARCHAR(100))"""
    conn.commit()
    conn.close()