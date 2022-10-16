-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Hotel
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Hotel
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Hotel` ;
USE `Hotel` ;

-- -----------------------------------------------------
-- Table `Hotel`.`Persona`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Hotel`.`Persona` (
  `idPersona` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  `Apellido` VARCHAR(45) NOT NULL,
  `FechaNac` DATE NOT NULL,
  `Tipo_Iden` VARCHAR(20) NOT NULL,
  `Numero_Iden` INT NOT NULL,
  `Email` VARCHAR(45) NOT NULL,
  `Pais` VARCHAR(15) NOT NULL,
  `Telefono` VARCHAR(25) NOT NULL,
  `Ciudad` VARCHAR(15) NOT NULL,
  `Password` VARCHAR(30) NOT NULL,
  `Usuario` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`idPersona`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Hotel`.`Habitacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Hotel`.`Habitacion` (
  `HabitacionNum` INT NOT NULL,
  `Piso` VARCHAR(15) NOT NULL,
  `Estado` VARCHAR(15) NOT NULL,
  `TipoHab` INT NOT NULL,
  PRIMARY KEY (`HabitacionNum`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Hotel`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Hotel`.`Usuario` (
  `idUsuario` INT NOT NULL,
  `Login` VARCHAR(10) NOT NULL,
  `Password` VARCHAR(25) NOT NULL,
  `Tipo_Usuario` VARCHAR(15) NOT NULL,
  `Email` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idUsuario`),
  CONSTRAINT `fk_idUsuario`
    FOREIGN KEY (`idUsuario`)
    REFERENCES `Hotel`.`Persona` (`idPersona`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Hotel`.`Reserva`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Hotel`.`Reserva` (
  `idReserva` INT NOT NULL AUTO_INCREMENT,
  `VIP` TINYINT NOT NULL,
  `HabitacionNum` INT NOT NULL,
  `idUsuario` INT NOT NULL,
  `Comentario` VARCHAR(100) NULL,
  `FechaEntrada` DATETIME NOT NULL,
  `FechaSalida` DATETIME NOT NULL,
  PRIMARY KEY (`idReserva`),
  INDEX `HabitacionNum_idx` (`HabitacionNum` ASC) VISIBLE,
  INDEX `fk_Usuario_idx` (`idUsuario` ASC) VISIBLE,
  CONSTRAINT `fk_HabitacionNum`
    FOREIGN KEY (`HabitacionNum`)
    REFERENCES `Hotel`.`Habitacion` (`HabitacionNum`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Usuario`
    FOREIGN KEY (`idUsuario`)
    REFERENCES `Hotel`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Hotel`.`Pago`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Hotel`.`Pago` (
  `idPago` INT NOT NULL AUTO_INCREMENT,
  `idReserva` INT NOT NULL,
  `Monto` FLOAT NOT NULL,
  `MetodoDePago` VARCHAR(45) NOT NULL,
  `NumComprobante` VARCHAR(20) NOT NULL,
  `IVA` FLOAT NOT NULL,
  `Fecha_Emision` DATE NOT NULL,
  PRIMARY KEY (`idPago`),
  UNIQUE INDEX `NumComprobante_UNIQUE` (`NumComprobante` ASC) VISIBLE,
  INDEX `fk_Reserva_idx` (`idReserva` ASC) VISIBLE,
  CONSTRAINT `fk_Reserva`
    FOREIGN KEY (`idReserva`)
    REFERENCES `Hotel`.`Reserva` (`idReserva`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
