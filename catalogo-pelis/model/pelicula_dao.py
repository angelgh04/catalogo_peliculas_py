from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    #Creamos un objeto de esta clase para obtener la conexión
    conexion = ConexionDB()
    #Código sql para crear tabla
    sql = '''
    CREATE TABLE peliculas(
        id_pelicula INTEGER,
        nombre VARCHAR(100),
        duracion VARCHAR(10),
        genero VARCHAR(100),
        
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )'''
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Crear Registro'
        mensaje = 'La tabla se creó correctamente'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'La tabla ya se encuentra creada'
        messagebox.showinfo(titulo, mensaje)
    
#Para eliminar tabla
def borrar_tabla():
    conexion = ConexionDB()
    
    sql = 'DROP TABLE peliculas'
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar Registro'
        mensaje = 'La tabla se borró correctamente'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Borraar Registro'
        mensaje = 'No hay tabla cargada'
        messagebox.showinfo(titulo, mensaje)
        
class Pelicula:
    #Definimos nuestro constructor
    def __init__(self, nombre, duracion, genero):
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
        
    def __str__(self):
        return f'Pelicula[{self.nombre},{self.duracion},{self.genero}]'
    
def guardar(pelicula):
    conexion = ConexionDB()
    
    sql = f"""INSERT INTO peliculas (nombre, duracion, genero)
    VALUES ('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}')"""
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'La tabla no esta creada'
        messagebox.showerror(titulo, mensaje)
        
def listar():
    conexion = ConexionDB()
    
    lista_peliculas = []
    sql = 'SELECT * FROM peliculas'
    
    try:
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
        
    except:
        titulo = 'Conexión al Registro'
        mensaje = 'Crea la tabla en la BBDD'
        messagebox.showwarning(titulo, mensaje)
        
    return lista_peliculas

def editar(pelicula, id_pelicula):
    conexion = ConexionDB()
    
    sql = f"""UPDATE peliculas
    SET nombre = '{pelicula.nombre}', duracion ='{pelicula.duracion}', genero = '{pelicula.genero}'
    WHERE id_pelicula = {id_pelicula}"""
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        
    except:
        titulo = 'Edición de Registro'
        mensaje = 'Error al editar registro'
        messagebox.showerror(titulo, mensaje)
        
def eliminar(id_pelicula):
    conexion = ConexionDB()
    sql = f'DELETE FROM peliculas WHERE id_pelicula = {id_pelicula}'
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        
    except:
        titulo = 'Eliminar Registro'
        mensaje = 'Error al eliminar registro'
        messagebox.showerror(titulo, mensaje)
    