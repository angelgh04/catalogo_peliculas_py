import sqlite3


class ConexionDB:
    #Abrimos la conexión a la BBDD
    def __init__(self):
        #Definimos el nombre de la BBDD. Si no existe lo crea y sino, lo abre.
        self.base_datos = 'catalogo-pelis/database/peliculas.db'
        #Definimos la variable que contendrá la conexión de la BBDD
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()
        
        
    #Cerramos la conexión
    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()