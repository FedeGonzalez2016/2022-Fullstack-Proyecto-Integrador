from conexion import conn

class InstalacionesTabla():
    cursor = conn.cursor()
    sql = """CREATE TABLE instalaciones (id INT AUTO_INCREMENT PRIMARY KEY,habitacion INT(12),estado VARCHAR(100),id_cliente number(12),tipo VARCHAR(100),piso INT(12))"""
    conn.commit()
    conn.close()