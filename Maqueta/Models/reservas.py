from conexion import conn

class ReservasTabla():
    cursor = conn.cursor()
    sql = """CREATE TABLE reservas (id_reserva INT AUTO_INCREMENT PRIMARY KEY,id_habitacion INT(12),id_usuario INT(12),id_cliente number(12),comentario VARCHAR(100),fecha_entrada DATE,fecha_salida DATE)"""
    conn.commit()
    conn.close()