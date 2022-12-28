-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Cinemas_of_Guatemala`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Cinemas_of_Guatemala` (
  `id_Cinemas_of_Guatemala` INT NOT NULL,
  `Region_Metropolitana` VARCHAR(45) NOT NULL,
  `Region_Norte` VARCHAR(45) NOT NULL,
  `Region_Nor_Oriente` VARCHAR(45) NOT NULL,
  `Region_Sur_Oriente` VARCHAR(45) NOT NULL,
  `Region_Central` VARCHAR(45) NOT NULL,
  `Region_Sur_Occidente` VARCHAR(45) NOT NULL,
  `Region_Occidente` VARCHAR(45) NOT NULL,
  `Region_De_Peten` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_Cinemas_of_Guatemala`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Film`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Film` (
  `id_Film` INT NOT NULL,
  `Qualification` VARCHAR(45) NOT NULL,
  `Url` VARCHAR(45) NOT NULL,
  `Classification` VARCHAR(45) NULL,
  PRIMARY KEY (`id_Film`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Cinemas_of_Guatemala_has_Lista_De_Peliculas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Cinemas_of_Guatemala_has_Lista_De_Peliculas` (
  `Cinemas_of_Guatemala_id_Cinemas_of_Guatemala` INT NOT NULL,
  `Lista_De_Peliculas_id_Lista_De_Peliculas` INT NOT NULL,
  PRIMARY KEY (`Cinemas_of_Guatemala_id_Cinemas_of_Guatemala`, `Lista_De_Peliculas_id_Lista_De_Peliculas`),
  INDEX `fk_Cinemas_of_Guatemala_has_Lista_De_Peliculas_Lista_De_Pel_idx` (`Lista_De_Peliculas_id_Lista_De_Peliculas` ASC) VISIBLE,
  INDEX `fk_Cinemas_of_Guatemala_has_Lista_De_Peliculas_Cinemas_of_G_idx` (`Cinemas_of_Guatemala_id_Cinemas_of_Guatemala` ASC) VISIBLE,
  CONSTRAINT `fk_Cinemas_of_Guatemala_has_Lista_De_Peliculas_Cinemas_of_Gua`
    FOREIGN KEY (`Cinemas_of_Guatemala_id_Cinemas_of_Guatemala`)
    REFERENCES `mydb`.`Cinemas_of_Guatemala` (`id_Cinemas_of_Guatemala`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Cinemas_of_Guatemala_has_Lista_De_Peliculas_Lista_De_Pelic1`
    FOREIGN KEY (`Lista_De_Peliculas_id_Lista_De_Peliculas`)
    REFERENCES `mydb`.`Film` (`id_Film`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Fucctions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Fucctions` (
  `id_ Functions` INT NOT NULL,
  `Date` VARCHAR(45) NOT NULL,
  `Hour` VARCHAR(45) NOT NULL,
  `Film_id_Film` INT NOT NULL,
  PRIMARY KEY (`id_ Functions`),
  INDEX `fk_Fucctions_Film1_idx` (`Film_id_Film` ASC) VISIBLE,
  CONSTRAINT `fk_Fucctions_Film1`
    FOREIGN KEY (`Film_id_Film`)
    REFERENCES `mydb`.`Film` (`id_Film`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Login`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Login` (
  `id_Login` INT NOT NULL,
  `E-mail` VARCHAR(45) NOT NULL,
  `User Password` VARCHAR(45) NOT NULL,
  `Token` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_Login`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Buy tickets`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Buy tickets` (
  `id_Buy tickets` INT NOT NULL,
  `selected seat` VARCHAR(45) NOT NULL,
  `Seat verification` VARCHAR(45) NOT NULL,
  `Buy ticketscol` VARCHAR(45) NOT NULL,
  `Fucctions_id_ Functions` INT NOT NULL,
  PRIMARY KEY (`id_Buy tickets`),
  INDEX `fk_Buy tickets_Fucctions1_idx` (`Fucctions_id_ Functions` ASC) VISIBLE,
  CONSTRAINT `fk_Buy tickets_Fucctions1`
    FOREIGN KEY (`Fucctions_id_ Functions`)
    REFERENCES `mydb`.`Fucctions` (`id_ Functions`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Consultation of purchased tickets`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Consultation of purchased tickets` (
  `id_Consultation of purchased tickets` INT NOT NULL,
  `id_ticket` INT NOT NULL,
  `Numero_De_Asiento` INT NOT NULL,
  `Buy tickets` INT NOT NULL,
  PRIMARY KEY (`id_Consultation of purchased tickets`),
  INDEX `fk_Consulta_De_Boletos_Comprados_Comprar_Boletos1_idx` (`Buy tickets` ASC) VISIBLE,
  CONSTRAINT `fk_Consulta_De_Boletos_Comprados_Comprar_Boletos1`
    FOREIGN KEY (`Buy tickets`)
    REFERENCES `mydb`.`Buy tickets` (`id_Buy tickets`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`User Registration`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`User Registration` (
  `id_User Registration` INT NOT NULL,
  `Login` INT NOT NULL,
  PRIMARY KEY (`id_User Registration`, `Login`),
  INDEX `fk_Registro_De_Usuarios_has_Inicio_De_Sesion_Inicio_De_Sesi_idx` (`Login` ASC) VISIBLE,
  INDEX `fk_Registro_De_Usuarios_has_Inicio_De_Sesion_Registro_De_Us_idx` (`id_User Registration` ASC) VISIBLE,
  CONSTRAINT `fk_Registro_De_Usuarios_has_Inicio_De_Sesion_Registro_De_Usua1`
    FOREIGN KEY (`id_User Registration`)
    REFERENCES `mydb`.`User Registration` (`id_User register`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Registro_De_Usuarios_has_Inicio_De_Sesion_Inicio_De_Sesion1`
    FOREIGN KEY (`Login`)
    REFERENCES `mydb`.`Login` (`id_Login`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Function`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Function` (
  `id_Function` INT NOT NULL,
  `id_Film` VARCHAR(45) NOT NULL,
  `Qualification` VARCHAR(45) NOT NULL,