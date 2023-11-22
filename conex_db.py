import mysql.connector


db = None
cursor = None

db_name = 'db_poo'


class database:

    db = None
    cursor = None

    def __init__(self):
        global cursor

        try:
            db = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                db='db_poo'
            )
            cursor = db.cursor()

            if db.is_connected():
                print("Conexion Exitosa....")

        except Exception as ex:
            print(ex)
            print("Error en la conexión a la base de datos")

    def createSchema():
        try:
            sql = "CREATE SCHEMA IF NOT EXISTS `vortex_ventures` DEFAULT CHARACTER SET utf8mb4 ;"
            cursor.execute(sql)
            sql = "USE vortex_ventures;"
            cursor.execute(sql)
        except Exception as ex:
            print(ex)
            print("Error al crear el esquema")

    def createTableAuto():
        sql = """CREATE TABLE IF NOT EXISTS `db_poo`.`autorizacion` (
                    id` INT(5) NOT NULL,
                    `revi_por` VARCHAR(100) NULL DEFAULT NULL,
                    `autori-por` VARCHAR(100) NULL DEFAULT NULL,
                    `requisicion_folio` VARCHAR(10) NOT NULL,
                    PRIMARY KEY (`id`),
                    INDEX `fk_autorizacion_requisicion1_idx` (`requisicion_folio`),
                        CONSTRAINT `fk_autorizacion_requisicion1`
                        FOREIGN KEY (`requisicion_folio`)
                        REFERENCES `db_poo`.`requisicion` (`folio`)
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION)
                ENGINE = InnoDB
                DEFAULT CHARACTER SET = utf8mb4;"""
        cursor.execute(sql)
        print("Tabla autorizacion creada con exito")

    def close_conex():
        if cursor:
            cursor.close()
        if db:
            db.close()


db = database()
