import mysql.connector


db = None
cursor = None

db_name = 'db_poo'


class database:

    db = None
    cursos = None

    def __init__(self):

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

    def crearTablas(self):
        sql = """ CREATE TABLE IF NOT EXISTS usuarios (
            
            """

    def close_conex():
        if cursor:
            cursor.close()
        if db:
            db.close()


db = database()
