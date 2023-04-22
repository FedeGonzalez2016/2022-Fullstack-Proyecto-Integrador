-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema hotelcalifornia
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema hotelcalifornia
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `hotelcalifornia` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `hotelcalifornia` ;

-- -----------------------------------------------------
-- Table `hotelcalifornia`.`TipoHabitacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotelcalifornia`.`TipoHabitacion` (
  `idTipoHabitacion` INT NOT NULL AUTO_INCREMENT,
  `Desc_Hab` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idTipoHabitacion`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hotelcalifornia`.`habitacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotelcalifornia`.`habitacion` (
  `HabitacionNum` INT NOT NULL,
  `Piso` VARCHAR(15) NOT NULL,
  `Estado` VARCHAR(15) NOT NULL,
  `TipoHabFK` INT NOT NULL,
  PRIMARY KEY (`HabitacionNum`),
  INDEX `Fk_TipoHab_idx` (`TipoHabFK` ASC) VISIBLE,
  CONSTRAINT `Fk_TipoHab`
    FOREIGN KEY (`TipoHabFK`)
    REFERENCES `hotelcalifornia`.`TipoHabitacion` (`idTipoHabitacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `hotelcalifornia`.`Metodo_Pago`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotelcalifornia`.`Metodo_Pago` (
  `idMetodo_Pago` INT NOT NULL AUTO_INCREMENT,
  `Desc_Metodo` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idMetodo_Pago`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hotelcalifornia`.`Ciudad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotelcalifornia`.`Ciudad` (
  `idCiudad` INT NOT NULL AUTO_INCREMENT,
  `Desc_Ciudad` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCiudad`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hotelcalifornia`.`Identificacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotelcalifornia`.`Identificacion` (
  `idIdentificacion` INT NOT NULL AUTO_INCREMENT,
  `Desc_Iden` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idIdentificacion`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hotelcalifornia`.`persona`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotelcalifornia`.`persona` (
  `idPersona` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(40) NOT NULL,
  `Apellido` VARCHAR(40) NOT NULL,
  `FechaNac` DATE NULL DEFAULT NULL,
  `Tipo_IdenFK` INT NULL DEFAULT NULL,
  `Numero_Iden` INT NULL DEFAULT NULL,
  `Email` VARCHAR(50) NOT NULL,
  `Pais` VARCHAR(20) NULL DEFAULT NULL,
  `Telefono` VARCHAR(25) NOT NULL,
  `CiudadFK` INT NOT NULL,
  `Password` VARCHAR(30) NOT NULL,
  `Usuario` VARCHAR(10) NULL DEFAULT NULL,
  PRIMARY KEY (`idPersona`),
  UNIQUE INDEX `Email_UNIQUE` (`Email` ASC) VISIBLE,
  INDEX `Fk_Ciudad_idx` (`CiudadFK` ASC) VISIBLE,
  INDEX `Fk_Tipo_Iden_idx` (`Tipo_IdenFK` ASC) VISIBLE,
  CONSTRAINT `Fk_Ciudad`
    FOREIGN KEY (`CiudadFK`)
    REFERENCES `hotelcalifornia`.`Ciudad` (`idCiudad`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Fk_Tipo_Iden`
    FOREIGN KEY (`Tipo_IdenFK`)
    REFERENCES `hotelcalifornia`.`Identificacion` (`idIdentificacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `hotelcalifornia`.`tipo_user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotelcalifornia`.`tipo_user` (
  `idUser` INT NOT NULL AUTO_INCREMENT,
  `Desc_User` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`idUser`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `hotelcalifornia`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotelcalifornia`.`usuario` (
  `idUsuario` INT NOT NULL AUTO_INCREMENT,
  `Login` VARCHAR(10) NOT NULL,
  `Password` VARCHAR(30) NOT NULL,
  `Tipo_UsuarioFK` INT NOT NULL,
  `Email` VARCHAR(50) NOT NULL,
  `idPersonaFK` INT NOT NULL,
  PRIMARY KEY (`idUsuario`),
  UNIQUE INDEX `Email` (`Email` ASC) VISIBLE,
  INDEX `Fk_Persona_idx` (`idPersonaFK` ASC) VISIBLE,
  INDEX `Fk_Tipo_Usuario_idx` (`Tipo_UsuarioFK` ASC) VISIBLE,
  CONSTRAINT `Fk_Persona`
    FOREIGN KEY (`idPersonaFK`)
    REFERENCES `hotelcalifornia`.`persona` (`idPersona`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Fk_Tipo_Usuario`
    FOREIGN KEY (`Tipo_UsuarioFK`)
    REFERENCES `hotelcalifornia`.`tipo_user` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `hotelcalifornia`.`reserva`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotelcalifornia`.`reserva` (
  `idReserva` INT NOT NULL AUTO_INCREMENT,
  `VIP` TINYINT(1) NOT NULL,
  `HabitacionNumFK` INT NOT NULL,
  `idUsuarioFK` INT NOT NULL,
  `Comentario` VARCHAR(100) NULL DEFAULT NULL,
  `FechaEntrada` DATETIME NOT NULL,
  `FechaSalida` DATETIME NOT NULL,
  PRIMARY KEY (`idReserva`),
  INDEX `Fk_Usuario_idx` (`idUsuarioFK` ASC) VISIBLE,
  INDEX `Fk_Habitacion_idx` (`HabitacionNumFK` ASC) VISIBLE,
  CONSTRAINT `Fk_Usuario`
    FOREIGN KEY (`idUsuarioFK`)
    REFERENCES `hotelcalifornia`.`usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Fk_Habitacion`
    FOREIGN KEY (`HabitacionNumFK`)
    REFERENCES `hotelcalifornia`.`habitacion` (`HabitacionNum`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `hotelcalifornia`.`pago`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotelcalifornia`.`pago` (
  `idPago` INT NOT NULL AUTO_INCREMENT,
  `idReservaFK` INT NOT NULL,
  `Monto` FLOAT NOT NULL,
  `MetodoDePagoFK` INT NOT NULL,
  `Fecha_emision` DATE NOT NULL,
  PRIMARY KEY (`idPago`),
  INDEX `Fk_MetodoDePago_idx` (`MetodoDePagoFK` ASC) VISIBLE,
  INDEX `Fk_Reserva_idx` (`idReservaFK` ASC) VISIBLE,
  CONSTRAINT `Fk_MetodoDePago`
    FOREIGN KEY (`MetodoDePagoFK`)
    REFERENCES `hotelcalifornia`.`Metodo_Pago` (`idMetodo_Pago`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Fk_Reserva`
    FOREIGN KEY (`idReservaFK`)
    REFERENCES `hotelcalifornia`.`reserva` (`idReserva`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
