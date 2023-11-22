import mysql.connector

class database:

    def __init__(self):
        self.db = None
        self.cursor = None

        try:
            self.db = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                db='db_poo'
            )
            
            self.cursor = self.db.cursor()

            if self.db.is_connected():
                print("Conexion Exitosa....")

        except Exception as ex:
            print(ex)
            print("Error en la conexión a la base de datos")
        
    def close_conex(self):
        if self.cursor:
            self.cursor.close()
        if self.db:
            self.db.close()

db = database()