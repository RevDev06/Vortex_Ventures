
CREATE SCHEMA IF NOT EXISTS `db_poo` DEFAULT CHARACTER SET utf8mb4 ;
USE `db_poo` ;
-- -----------------------------------------------------
-- Table `db_poo`.`autorizacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_poo`.`autorizacion` (
  `id` varchar(50),
  `revi_por` VARCHAR(100) not NULL,
  `autori_por` VARCHAR(100) not NULL,
  `requisicion_folio` VARCHAR(10) NOT NULL);
-- -----------------------------------------------------
-- Table `db_poo`.`candidatos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_poo`.`candidatos` (
  `id` varchar(50) NOT NULL,
  `nombre` VARCHAR(50) NOT NULL,
  `a_materno` VARCHAR(50) NOT NULL,
  `a_paterno` VARCHAR(50) NOT NULL,
  `num_telefono` VARCHAR(20) NOT NULL,
  `edad` varchar(50)NOT NULL,
  `correo_electronico` varchar(50) not null,
  `direccion` varchar(200) not null,
  `puesto` varchar(50) NOT NULL,
  `carrera` varchar(50) NOT NULL,
  `g_avance` varchar(50) NOT NULL,
  `e_civil` varchar(50) NOT NULL,
  `escolar` varchar(50) NOT NULL,
  `habil` varchar(50) NOT NULL,
  `sexo` varchar(50) NOT NULL);
-- -----------------------------------------------------
-- Table `db_poo`.`carrera`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_poo`.`carrera` (
  `id` varchar(50) NOT NULL,
  `nombre` VARCHAR(70) not NULL);
-- -----------------------------------------------------
-- Table `db_poo`.`doc_solicit`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_poo`.`doc_solicit` (
  `id` varchar(50) NOT NULL,
  `docum` VARCHAR(50) not NULL);
-- -----------------------------------------------------
-- Table `db_poo`.`e_civil`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_poo`.`e_civil` (
  `id` varchar(50) NOT NULL,
  `estado` VARCHAR(50) not NULL);
-- -----------------------------------------------------
-- Table `db_poo`.`edad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_poo`.`edad` (
  `id` varchar(50) NOT NULL,
  `edad` VARCHAR(20) Not NULL);
-- -----------------------------------------------------
-- Table `db_poo`.`escolar`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_poo`.`escolar` (
  `id` varchar(50) NOT NULL,
  `grado` VARCHAR(50) Not NULL);
-- -----------------------------------------------------
-- Table `db_poo`.`g_avance`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_poo`.`g_avance` (
  `id` varchar(50) NOT NULL,
  `grado` VARCHAR(50) Not NULL);
-- -----------------------------------------------------
-- Table `db_poo`.`habil`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_poo`.`habil` (
  `id` varchar(50) NOT NULL,
  `descrip` VARCHAR(70) Not NULL);
-- -----------------------------------------------------
-- Table `db_poo`.`med_public`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_poo`.`med_public` (
  `id` varchar(50) NOT NULL,
  `medio` VARCHAR(50) Not NULL);
-- -----------------------------------------------------
-- Table `db_poo`.`sexo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_poo`.`sexo` (
  `id` varchar(50) NOT NULL,
  `genero` VARCHAR(20) Not NULL);
-- -----------------------------------------------------
-- Table `db_poo`.`puesto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_poo`.`puesto` (
    `id` varchar(50) NOT NULL,
    `codigo` VARCHAR(10),
    `nombre` VARCHAR(100),
    `p_jefe` VARCHAR(50),
    `jorn` VARCHAR(50),
    `sueldo` varchar(50),
    `presta` VARCHAR(50),
    `desc_gen` VARCHAR(50),
    `funcion` VARCHAR(200),
    `exp` VARCHAR(30),
    `conoci` VARCHAR(50),
    `manejo_equipo` VARCHAR(100),
    `r_fisicos` VARCHAR(100),
    `r_psico` VARCHAR(100),
    `responsa` VARCHAR(100),
    `cond_tra` VARCHAR(50),
    `idioma` VARCHAR(25),
    `e_civil` varchar(150),
    `areas` varchar(50),
    `escolar` varchar(50),
    `edad` varchar(50),
    `sexo` varchar(50),
    `carrera` varchar(50),
    `g_avance` varchar(50),
    `habil` varchar(50),
	`doc_solicit` varchar(50));
-- -----------------------------------------------------
-- Table `db_poo`.`v_gene_por`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_poo`.`v_gene_por` (
  `id` varchar(50) NOT NULL,
  `por` VARCHAR(50) Not NULL);
-- -----------------------------------------------------
-- Table `db_poo`.`tipo_vacante`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_poo`.`tipo_vacante` (
  `id` varchar(50) NOT NULL,
  `tipo` VARCHAR(50) Not NULL);
  -- -----------------------------------------------------
-- Table `db_poo`.`area`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_poo`.`area` (
  `id` varchar(50) NOT NULL,
  `area` VARCHAR(50) Not NULL);
-- -----------------------------------------------------
-- Table `db_poo`.`requisicion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_poo`.`requisicion` (
  `folio` VARCHAR(10) NOT NULL,
  `fechaEla` DATE not NULL,
  `nombre` VARCHAR(50) not NULL,
  `puesto` VARCHAR(50) not NULL,
  `area` VARCHAR(50) not NULL,
  `fechaReclu` DATE not NULL,
  `fechaInicio` DATE not NULL,
  `num_vacantes` varchar(50) not NULL,
  `v_gene_por` varchar(50) NOT NULL,
  `tipo_vacante_id` varchar(50) NOT NULL,
  `autorizacion_id` varchar(50) NOT NULL,
  `puesto_id` varchar(50) NOT NULL,
  `areas_id` varchar(50) NOT NULL,
  `med_public_id` varchar(50) NOT NULL,
  PRIMARY KEY (`folio`));
-- -----------------------------------------------------
-- Table `db_poo`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_poo`.`usuarios` (
  `id` INT(10) NOT NULL AUTO_INCREMENT,
  `correo` VARCHAR(100) not NULL,
  `nombre` VARCHAR(50) Not NULL,
  `contrasenia` VARCHAR(255) not NULL,
  PRIMARY KEY (`id`));
-- -----------------------------------------------------
-- Table `db_poo`.`vacantes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_poo`.`vacantes` (
  `id` INT(5) NOT NULL);

use db_poo;
insert into usuarios(nombre, correo, contrasenia) values ('mayrin', 'mayrinreyes1707@gmail.com', '12345');
