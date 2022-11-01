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

