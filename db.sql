-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS
, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS
, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE
, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema db_poo
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema db_poo
-- -----------------------------------------------------
CREATE SCHEMA
IF NOT EXISTS db_poo DEFAULT CHARACTER
SET utf8mb4 ;
USE db_poo
;

-- -----------------------------------------------------
-- Table db_poo.autorizacion
-- -----------------------------------------------------
CREATE TABLE
IF NOT EXISTS db_poo.autorizacion
(
  id INT
(5) NOT NULL,
  revi_por VARCHAR
(100) NULL DEFAULT NULL,
  autori-por VARCHAR
(100) NULL DEFAULT NULL,
  requisicion_folio VARCHAR
(10) NOT NULL,
  PRIMARY KEY
(id),
  INDEX fk_autorizacion_requisicion1_idx
(requisicion_folio),
  CONSTRAINT fk_autorizacion_requisicion1
    FOREIGN KEY
(requisicion_folio)
    REFERENCES db_poo.requisicion
(folio)
    ON
DELETE NO ACTION
    ON
UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER
SET = utf8mb4;


-- -----------------------------------------------------
-- Table db_poo.autorizacion
-- -----------------------------------------------------
CREATE TABLE
IF NOT EXISTS db_poo.autorizacion
(
  id INT
(5) NOT NULL,
  revi_por VARCHAR
(100) NULL DEFAULT NULL,
  autori-por VARCHAR
(100) NULL DEFAULT NULL,
  PRIMARY KEY
(id))
ENGINE = InnoDB
DEFAULT CHARACTER
SET = utf8mb4;


-- -----------------------------------------------------
-- Table db_poo.candidatos
-- -----------------------------------------------------
CREATE TABLE
IF NOT EXISTS db_poo.candidatos
(
  id INT
(5) NOT NULL,
  PRIMARY KEY
(id))
ENGINE = InnoDB
DEFAULT CHARACTER
SET = utf8mb4;


-- -----------------------------------------------------
-- Table db_poo.carrera
-- -----------------------------------------------------
CREATE TABLE
IF NOT EXISTS db_poo.carrera
(
  id INT
(5) NOT NULL,
  nombre VARCHAR
(70) NULL DEFAULT NULL,
  PRIMARY KEY
(id))
ENGINE = InnoDB
DEFAULT CHARACTER
SET = utf8mb4;


-- -----------------------------------------------------
-- Table db_poo.doc_solicit
-- -----------------------------------------------------
CREATE TABLE
IF NOT EXISTS db_poo.doc_solicit
(
  id INT
(5) NOT NULL,
  docum VARCHAR
(50) NULL DEFAULT NULL,
  PRIMARY KEY
(id))
ENGINE = InnoDB
DEFAULT CHARACTER
SET = utf8mb4;


-- -----------------------------------------------------
-- Table db_poo.e_civil
-- -----------------------------------------------------
CREATE TABLE
IF NOT EXISTS db_poo.e_civil
(
  id INT
(5) NOT NULL,
  estado VARCHAR
(50) NULL DEFAULT NULL,
  PRIMARY KEY
(id))
ENGINE = InnoDB
DEFAULT CHARACTER
SET = utf8mb4;


-- -----------------------------------------------------
-- Table db_poo.edad
-- -----------------------------------------------------
CREATE TABLE
IF NOT EXISTS db_poo.edad
(
  id INT
(5) NOT NULL,
  edad VARCHAR
(20) NULL DEFAULT NULL,
  PRIMARY KEY
(id))
ENGINE = InnoDB
DEFAULT CHARACTER
SET = utf8mb4;


-- -----------------------------------------------------
-- Table db_poo.escolar
-- -----------------------------------------------------
CREATE TABLE
IF NOT EXISTS db_poo.escolar
(
  id INT
(5) NOT NULL,
  grado VARCHAR
(50) NULL DEFAULT NULL,
  PRIMARY KEY
(id))
ENGINE = InnoDB
DEFAULT CHARACTER
SET = utf8mb4;


-- -----------------------------------------------------
-- Table db_poo.g_avance
-- -----------------------------------------------------
CREATE TABLE
IF NOT EXISTS db_poo.g_avance
(
  id INT
(5) NOT NULL,
  grado VARCHAR
(50) NULL DEFAULT NULL,
  PRIMARY KEY
(id))
ENGINE = InnoDB
DEFAULT CHARACTER
SET = utf8mb4;


-- -----------------------------------------------------
-- Table db_poo.habil
-- -----------------------------------------------------
CREATE TABLE
IF NOT EXISTS db_poo.habil
(
  id INT
(5) NOT NULL,
  descrip VARCHAR
(70) NULL DEFAULT NULL,
  PRIMARY KEY
(id))
ENGINE = InnoDB
DEFAULT CHARACTER
SET = utf8mb4;


-- -----------------------------------------------------
-- Table db_poo.med_public
-- -----------------------------------------------------
CREATE TABLE
IF NOT EXISTS db_poo.med_public
(
  id INT
(5) NOT NULL,
  medio VARCHAR
(50) NULL DEFAULT NULL,
  PRIMARY KEY
(id))
ENGINE = InnoDB
DEFAULT CHARACTER
SET = utf8mb4;


-- -----------------------------------------------------
-- Table db_poo.sexo
-- -----------------------------------------------------
CREATE TABLE
IF NOT EXISTS db_poo.sexo
(
  id INT
(5) NOT NULL,
  genero VARCHAR
(20) NULL DEFAULT NULL,
  PRIMARY KEY
(id))
ENGINE = InnoDB
DEFAULT CHARACTER
SET = utf8mb4;


-- -----------------------------------------------------
-- Table db_poo.puesto
-- -----------------------------------------------------
CREATE TABLE
IF NOT EXISTS db_poo.puesto
(
    id INT
(5) NOT NULL,
    codigo VARCHAR
(10) NULL DEFAULT NULL,
    nombre VARCHAR
(100) NULL DEFAULT NULL,
    p_jefe VARCHAR
(50) NULL DEFAULT NULL,
    jorn VARCHAR
(50) NULL DEFAULT NULL,
    sueldo INT
(7) NULL DEFAULT NULL,
    presta VARCHAR
(50) NULL DEFAULT NULL,
    desc_gen VARCHAR
(50) NULL DEFAULT NULL,
    funcion VARCHAR
(200) NULL DEFAULT NULL,
    exp VARCHAR
(30) NULL DEFAULT NULL,
    conoci VARCHAR
(50) NULL DEFAULT NULL,
    manejo_equipo VARCHAR
(100) NULL DEFAULT NULL,
    r_fisicos VARCHAR
(100) NULL DEFAULT NULL,
    r_psico VARCHAR
(100) NULL DEFAULT NULL,
    responsa VARCHAR
(100) NULL DEFAULT NULL,
    cond_tra VARCHAR
(50) NULL DEFAULT NULL,
    idioma VARCHAR
(25) NULL DEFAULT NULL,
    e_civil_id INT
(5) NOT NULL,
    areas_id INT
(5) NOT NULL,
    escolar_id INT
(5) NOT NULL,
    edad_id INT
(5) NOT NULL,
    sexo_id INT
(5) NOT NULL,
    carrera_id INT
(5) NOT NULL,
    g_avance_id INT
(5) NOT NULL,
    habil_id INT
(5) NOT NULL,
    PRIMARY KEY
(id),
    INDEX fk_puesto_e_civil_idx
(e_civil_id),
    INDEX fk_puesto_areas1_idx
(areas_id),
    INDEX fk_puesto_escolar1_idx
(escolar_id),
    INDEX fk_puesto_edad1_idx
(edad_id),
    INDEX fk_puesto_sexo1_idx
(sexo_id),
    INDEX fk_puesto_carrera1_idx
(carrera_id),
    INDEX fk_puesto_g_avance1_idx
(g_avance_id),
    INDEX fk_puesto_habil1_idx
(habil_id),
    CONSTRAINT fk_puesto_e_civil
        FOREIGN KEY
(e_civil_id)
        REFERENCES db_poo.e_civil
(id)
        ON
DELETE NO ACTION
        ON
UPDATE NO ACTION,
    CONSTRAINT fk_puesto_areas1
FOREIGN KEY
(areas_id)
        REFERENCES db_poo.areas
(id)
        ON
DELETE NO ACTION
        ON
UPDATE NO ACTION,
    CONSTRAINT fk_puesto_escolar1
FOREIGN KEY
(escolar_id)
        REFERENCES db_poo.escolar
(id)
        ON
DELETE NO ACTION
        ON
UPDATE NO ACTION,
    CONSTRAINT fk_puesto_edad1
FOREIGN KEY
(edad_id)
        REFERENCES db_poo.edad
(id)
        ON
DELETE NO ACTION
        ON
UPDATE NO ACTION,
    CONSTRAINT fk_puesto_sexo1
FOREIGN KEY
(sexo_id)
        REFERENCES db_poo.sexo
(id)
        ON
DELETE NO ACTION
        ON
UPDATE NO ACTION,
    CONSTRAINT fk_puesto_carrera1
FOREIGN KEY
(carrera_id)
        REFERENCES db_poo.carrera
(id)
        ON
DELETE NO ACTION
        ON
UPDATE NO ACTION,
    CONSTRAINT fk_puesto_g_avance1
FOREIGN KEY
(g_avance_id)
        REFERENCES db_poo.g_avance
(id)
        ON
DELETE NO ACTION
        ON
UPDATE NO ACTION,
    CONSTRAINT fk_puesto_habil1
FOREIGN KEY
(habil_id)
        REFERENCES db_poo.habil
(id)
        ON
DELETE NO ACTION
        ON
UPDATE NO ACTION
) ENGINE = InnoDB
DEFAULT CHARACTER
SET = utf8mb4;


-- -----------------------------------------------------
-- Table db_poo.v_gene_por
-- -----------------------------------------------------
CREATE TABLE
IF NOT EXISTS db_poo.v_gene_por
(
  id INT
(5) NOT NULL AUTO_INCREMENT,
  por VARCHAR
(50) NULL DEFAULT NULL,
  PRIMARY KEY
(id))
ENGINE = InnoDB
DEFAULT CHARACTER
SET = utf8mb4;


-- -----------------------------------------------------
-- Table db_poo.tipo_vacante
-- -----------------------------------------------------
CREATE TABLE
IF NOT EXISTS db_poo.tipo_vacante
(
  id INT
(5) NOT NULL,
  tipo VARCHAR
(50) NULL DEFAULT NULL,
  PRIMARY KEY
(id))
ENGINE = InnoDB
DEFAULT CHARACTER
SET = utf8mb4;


-- -----------------------------------------------------
-- Table db_poo.requisicion
-- -----------------------------------------------------
CREATE TABLE
IF NOT EXISTS db_poo.requisicion
(
  folio VARCHAR
(10) NOT NULL,
  fechaEla DATE NULL DEFAULT NULL,
  nombre VARCHAR
(50) NULL DEFAULT NULL,
  puesto VARCHAR
(50) NULL DEFAULT NULL,
  area VARCHAR
(50) NULL DEFAULT NULL,
  fechaReclu DATE NULL DEFAULT NULL,
  fechaInicio DATE NULL DEFAULT NULL,
  num_vacantes INT
(10) NULL DEFAULT NULL,
  v_gene_por_id INT
(5) NOT NULL,
  tipo_vacante_id INT
(5) NOT NULL,
  autorizacion_id INT
(5) NOT NULL,
  puesto_id INT
(5) NOT NULL,
  areas_id INT
(5) NOT NULL,
  PRIMARY KEY
(folio),
  INDEX fk_requisicion_v_gene_por1_idx
(v_gene_por_id),
  INDEX fk_requisicion_tipo_vacante1_idx
(tipo_vacante_id),
  INDEX fk_requisicion_autorizacion1_idx
(autorizacion_id),
  INDEX fk_requisicion_puesto1_idx
(puesto_id),
  INDEX fk_requisicion_areas1_idx
(areas_id),
  CONSTRAINT fk_requisicion_v_gene_por1
    FOREIGN KEY
(v_gene_por_id)
    REFERENCES db_poo.v_gene_por
(id)
    ON
DELETE NO ACTION
    ON
UPDATE NO ACTION,
  CONSTRAINT fk_requisicion_tipo_vacante1
FOREIGN KEY
(tipo_vacante_id)
    REFERENCES db_poo.tipo_vacante
(id)
    ON
DELETE NO ACTION
    ON
UPDATE NO ACTION,
  CONSTRAINT fk_requisicion_autorizacion1
FOREIGN KEY
(autorizacion_id)
    REFERENCES db_poo.autorizacion
(id)
    ON
DELETE NO ACTION
    ON
UPDATE NO ACTION,
  CONSTRAINT fk_requisicion_puesto1
FOREIGN KEY
(puesto_id)
    REFERENCES db_poo.puesto
(id)
    ON
DELETE NO ACTION
    ON
UPDATE NO ACTION,
  CONSTRAINT fk_requisicion_areas1
FOREIGN KEY
(areas_id)
    REFERENCES db_poo.areas
(id)
    ON
DELETE NO ACTION
    ON
UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER
SET = utf8mb4;


-- -----------------------------------------------------
-- Table db_poo.usuarios
-- -----------------------------------------------------
CREATE TABLE
IF NOT EXISTS db_poo.usuarios
(
  id INT
(10) NOT NULL AUTO_INCREMENT,
  correo VARCHAR
(100) NULL DEFAULT NULL,
  nombre VARCHAR
(50) NULL DEFAULT NULL,
  contrasenia VARCHAR
(50) NULL DEFAULT NULL,
  PRIMARY KEY
(id))
ENGINE = InnoDB
DEFAULT CHARACTER
SET = utf8mb4;

-- -----------------------------------------------------
-- Table db_poo.vacantes
-- -----------------------------------------------------
CREATE TABLE
IF NOT EXISTS db_poo.vacantes
(
  id INT
(5) NOT NULL,
  PRIMARY KEY
(id))
ENGINE = InnoDB
DEFAULT CHARACTER
SET = utf8mb4;


SET SQL_MODE
=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS
=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS
=@OLD_UNIQUE_CHECKS;