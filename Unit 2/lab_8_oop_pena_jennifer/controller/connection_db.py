import mysql.connector
from mysql.connector import Error
from controller.config import DB_CONFIG

class Database_connection:
    def __init__(self):
        self.host = DB_CONFIG["host"]
        self.usuario = DB_CONFIG["user"]
        self.password = DB_CONFIG["password"]
        self.base_datos = DB_CONFIG["database"]

    def conectar(self):
        try:
            conexion = mysql.connector.connect(
                host=self.host,
                user=self.usuario,
                password=self.password,
                database=self.base_datos
            )
            return conexion
        except Error as error:
            print("Error al conectar con MySQL:", error)
            return None