use HotelCalifornia;

insert into ciudad (Desc_Ciudad) value ('Buenos Aires');
insert into ciudad (Desc_Ciudad) value ('Cordoba');
insert into ciudad (Desc_Ciudad) value ('La Plata');
insert into ciudad (Desc_Ciudad) value ('Rosario');
insert into ciudad (Desc_Ciudad) value ('Villa Carlos Paz');
insert into ciudad (Desc_Ciudad) value ('Misiones');

select * from ciudad;
-- ---------------------------------------------------------------------------------------------------------------------
insert into metodo_pago (Desc_Metodo) value ('Mastercard');
insert into metodo_pago (Desc_Metodo) value ('Mercado Pago');
insert into metodo_pago (Desc_Metodo) value ('Visa');
insert into metodo_pago (Desc_Metodo) value ('Paypal');

select * from metodo_pago;
-- ---------------------------------------------------------------------------------------------------------------------

insert into tipo_user (Desc_user) value ('Recepcionista');
insert into tipo_user (Desc_user) value ('Gerente');
insert into tipo_user (Desc_user) value ('Tecnico');
insert into tipo_user (Desc_user) value ('Cliente');

select * from tipo_user;
-- ---------------------------------------------------------------------------------------------------------------------
insert into persona (Nombre, Apellido, Email, Telefono,  Password, CiudadFK ) value ('Agustin', 'Bengolea', 'agustinbengolea97@gmail.com', '1150217843', '54321', 1);
insert into usuario (Login, Password, Tipo_UsuarioFK, Email, idPersonaFK) value ('admin', '54321', 1, 'agustinbengolea97@gmail.com', 1);

update usuario set Tipo_UsuarioFK = 2 where idUsuario = 1;

select * from usuario;
select Nombre, Desc_Ciudad
from persona inner join ciudad on persona.CiudadFK=ciudad.idCiudad;
