-- Crear la base de datos "database_hotel"
CREATE DATABASE database_hotel;

-- Usar la base de datos "database_hotel"
USE database_hotel;

-- Crear la tabla "hotel"
CREATE TABLE hotel (
  Hotel_Id INT PRIMARY KEY AUTO_INCREMENT,
  Hotel_RazonSocial VARCHAR(50),
  Hotel_Cuil INT(20),
  Hotel_Domicilio VARCHAR(50),
  Hotel_Localidad VARCHAR(50),
  Hotel_Provincia VARCHAR(50),
  Hotel_CP INT(20),
  Hotel_Telefono INT(50),
  Hotel_Categoria VARCHAR(50),
  Hotel_Email VARCHAR(50)
);

-- Crear la tabla "empleado"
CREATE TABLE empleado (
  Empleadoid INT PRIMARY KEY AUTO_INCREMENT,
  Empleado_Nombre VARCHAR(50),
  Empleado_Apellido VARCHAR(50),
  Empleado_Usuario VARCHAR(50),
  Empleado_Correo VARCHAR(50),
  Empleado_Password VARCHAR(50),
  Empleado_Domicilio VARCHAR(50),
  Empleado_Localidad VARCHAR(50),
  Empleado_Provincia VARCHAR(50),
  Empleado_CP INT(20),
  Empleado_Telefono INT(20),
  Empleado_Password VARCHAR(50),
  Empleado_Rol VARCHAR(50),
  FOREIGN KEY (Hotel_Id) REFERENCES hotel(Hotel_Id)
);

-- Crear la tabla "habitacion"
CREATE TABLE habitacion (
  Habitacion_Id INT PRIMARY KEY AUTO_INCREMENT,
  Habitacion_Numero INT(20),
  Habitacion_Piso INT(20),
  Habitacion_Estado VARCHAR(50),
  Habitacion_Precio INT(20),
  FOREIGN KEY (Hotel_Id) REFERENCES hotel(Hotel_Id),
  FOREIGN KEY (Tipo_Id) REFERENCES tipo(Tipo_Id)
);

-- Crear la tabla "tipo"
CREATE TABLE tipo (
  Tipo_Id INT PRIMARY KEY AUTO_INCREMENT,
  TIpo_Descripcion VARCHAR(50)
);

-- Crear la tabla "factura"
CREATE TABLE factura (
  Factura_Id INT PRIMARY KEY AUTO_INCREMENT,
  Factura_Numero INT(50),
  FOREIGN KEY (Hotel_Id) REFERENCES hotel(Hotel_Id),
  FOREIGN KEY (Cliente_Id) REFERENCES cliente(Cliente_Id)
);

-- Crear la tabla "cliente"
CREATE TABLE cliente (
  Cliente_Id INT PRIMARY KEY AUTO_INCREMENT,
  Cliente_Nombre VARCHAR(50),
  Cliente_Apellido VARCHAR(50),
  Cliente_Correo VARCHAR(50),
  Cliente_Password VARCHAR(50),
  Cliente_Nacimiento DATE(20)
);

-- Crear la tabla "reserva"
CREATE TABLE reserva (
  Reserva_Id INT PRIMARY KEY AUTO_INCREMENT,
  Fecha_Reserva DATE(20),
  FOREIGN KEY (Cliente_Id) REFERENCES cliente(Cliente_Id)
);

-- Crear la tabla "detalle"
CREATE TABLE detalle (
  Detalle_Id INT PRIMARY KEY AUTO_INCREMENT,
  Detalle_Descuento VARCHAR(50),
  Detalle_Importe INT(50),
  FOREIGN KEY (Factura_Id) REFERENCES factura(Factura_Id),
  FOREIGN KEY (Reserva_Id) REFERENCES reserva(Reserva_Id)
);

-- Crear la tabla "reserva_habitacion"
CREATE TABLE reserva_habitacion (
  Reserva_Habitacion_Id INT PRIMARY KEY AUTO_INCREMENT,
  Fecha_Ingreso DATE(20),
  Fecha_Egreso DATE(20),
  FOREIGN KEY (Habitacion_Id) REFERENCES factura(Factura_Id),
  FOREIGN KEY (Reserva_Id) REFERENCES reserva(Reserva_Id)
);

-- Crear la tabla "tipo_pago"
CREATE TABLE tipo_pago (
  Tipo_Pago_Id INT PRIMARY KEY AUTO_INCREMENT,
  Tipo VARCHAR(50)
);

-- Crear la tabla "detalle_pago"
CREATE TABLE reserva_habitacion (
  Detalle_Pago_Id INT PRIMARY KEY AUTO_INCREMENT,
  Porcentaje_Pago VARCHAR(50),
  FOREIGN KEY (Factura_Id) REFERENCES factura(Factura_Id),
  FOREIGN KEY (Tipo_Pago_Id) REFERENCES tipo_pago(Tipo_Pago_Id)
);



