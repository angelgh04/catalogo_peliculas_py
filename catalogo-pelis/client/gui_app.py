import tkinter as tk
#Importamos para trabajar con las tablas
from tkinter import ttk
from model.pelicula_dao import crear_tabla, borrar_tabla
from model.pelicula_dao import Pelicula, guardar, listar, editar, eliminar

#Definimos la función barra_menu que recibe el root (que es la raíz o ventana)
def barra_menu(root):
    #Definimos el objeto barra_menu
    barra_menu = tk.Menu(root)
    #Ancalamos la barra al root con un tamaño definido
    root.config(menu = barra_menu, width=300, height=300)
    
    #Definimos las opciones de la barra de menú
    #Creamos el menú Inicio y lo anclamos a la barra
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    #Agregamos a la barra
    barra_menu.add_cascade(label = 'Inicio', menu = menu_inicio)
    #Agregamos los submenú del menú Inicio
    menu_inicio.add_command(label='Nuevo Registro', command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Registro', command=borrar_tabla)
    #La opción Salir le agregamos el evento destroy para cerrar la ventana
    menu_inicio.add_command(label='Salir', command =root.destroy)
    
    #Agregamos a la barra de menú otras opciones
    barra_menu.add_cascade(label = 'Consultas')
    barra_menu.add_cascade(label = 'Configuración')
    barra_menu.add_cascade(label = 'Ayuda')

#Definimos el objeto Frame que sera la clase padre
class Frame(tk.Frame):
    #Definimos el constructor que recibe la raíz o ventana "root=None"
    def __init__(self, root = None):
        #Usamos la función super() para heredar el constructor de la clase padre
        #Le vamos a enviar el root o raíz que vamos a recibir y la configuración
        super().__init__(root, width=480, height=320)
        #Creamos el atributo raíz root inicializado en root
        self.root = root
        #Empaquetamos
        self.pack()
        #self.config(bg='blue')
        self.id_pelicula = None
        
        self.campos_pelis()
        self.deshabilitar_campos()
        self.tabla_peliculas()
        
    def campos_pelis(self):
        #Definimos las etiquetas Nombre, Duración y Género
        self.label_nombre = tk.Label(self, text = 'Nombre: ')
        self.label_nombre.config(font = ('Carlito', 12, 'bold'))
        #Definimos la posición en el frame usando las grillas con grid
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)
        
        self.label_nombre = tk.Label(self, text = 'Duración: ')
        self.label_nombre.config(font = ('Carlito', 12, 'bold'))
        self.label_nombre.grid(row=1, column=0, padx=10, pady=10)
        
        self.label_nombre = tk.Label(self, text = 'Género: ')
        self.label_nombre.config(font = ('Carlito', 12, 'bold'))
        self.label_nombre.grid(row=2, column=0, padx=10, pady=10)
        
        #Definimos los cuadro de textos para cada uno de las etiquetas
        #Definimos el objeto para enviar valores a los campos
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50, font=('Carlito', 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
        
        self.mi_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable=self.mi_duracion)
        self.entry_duracion.config(width=50, font=('Carlito', 12))
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
        
        self.mi_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self, textvariable=self.mi_genero)
        self.entry_genero.config(width=50, font=('Carlito', 12))
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10, columnspan=2)
        
        #Definimos los botones
        #Nuevo
        self.boton_nuevo = tk.Button(self, text = "Nuevo", command=self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial', 12,'bold'), fg='#FAFAFA', bg='#BD9240', cursor='hand2', activebackground='#F6F098')
        self.boton_nuevo.grid(row=3, column=0, padx=10, pady=10)
        
        #Guardar
        self.boton_guardar = tk.Button(self, text = "Guardar", command=self.guardar_datos)
        self.boton_guardar.config(width=20, font=('Arial', 12,'bold'), fg='#FAFAFA', bg='#158645', cursor='hand2', activebackground='#35BD6F')
        self.boton_guardar.grid(row=3, column=1, padx=10, pady=10)
        
        #Cancelar
        self.boton_cancelar = tk.Button(self, text = "Cancelar", command=self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Arial', 12,'bold'), fg='#FAFAFA', bg='#BD152E', cursor='hand2', activebackground='#35BD6F')
        self.boton_cancelar.grid(row=3, column=2, padx=10, pady=10)
        
    #Definimos los métodos para dar función a los botones
    def habilitar_campos(self):
        #Limpiamos los campos al inicar nuevo
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')
        
        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')
            
        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')        
        
    def deshabilitar_campos(self):
        self.id_pelicula = None
        #Limpiamos los campos al cancelar
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')
        
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')
        
        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')
    
    def guardar_datos(self):
        pelicula = Pelicula(
            self.mi_nombre.get(),
            self.mi_duracion.get(),
            self.mi_genero.get(),
        )
        
        if self.id_pelicula == None:
            guardar(pelicula)
        else:
            editar(pelicula, self.id_pelicula)
            
        #Cargamos de nuevo la tabla para que se acutalice el registro
        self.tabla_peliculas()
        
        self.deshabilitar_campos()
        
    #Diseñamos la tabla para mostrar los registros
    def tabla_peliculas(self):
        #Recuperamos la lista para mostrar
        self.lista_peliculas = listar()
        #Para que se muestre de menor a mayor
        self.lista_peliculas.reverse()
        
        self.tabla = ttk.Treeview(self, column=('Nombre', 'Duración', 'Genero'))
        #Indicamos en que parte estará la grilla
        self.tabla.grid(row=4, column=0, columnspan=4, sticky='nse')
        
        #Insertamos un scroll para varios registros
        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=4, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)
        
        #Título de las columnas de la tabla
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='DURACIÓN')
        self.tabla.heading('#3', text='GÉNERO')
        
        #Insertamos cada uno de los registros con un for
        for p in self.lista_peliculas:
            self.tabla.insert('', 0, text=p[0], values=(p[1], p[2], p[3]))
        
        
        #Botones de la tabla
        #Editar
        self.boton_editar = tk.Button(self, text = "Editar", command=self.editar_datos)
        self.boton_editar.config(width=20, font=('Arial', 12,'bold'), fg='#DAD5D6', bg='#158645', cursor='hand2', activebackground='#35BD6F')
        self.boton_editar.grid(row=5, column=0, padx=10, pady=10)
        
        #Cancelar
        self.boton_eliminar = tk.Button(self, text = "Eliminar", command=self.eliminar_datos)
        self.boton_eliminar.config(width=20, font=('Arial', 12,'bold'), fg='#DAD5D6', bg='#BD152E', cursor='hand2', activebackground='#35BD6F')
        self.boton_eliminar.grid(row=5, column=1, padx=10, pady=10)

    def editar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            self.nombre_pelicula = self.tabla.item(self.tabla.selection())['values'][0]
            self.duracion_pelicula = self.tabla.item(self.tabla.selection())['values'][1]
            self.genero_pelicula = self.tabla.item(self.tabla.selection())['values'][2]
            
            self.habilitar_campos()
            
            self.entry_nombre.insert(0, self.nombre_pelicula)
            self.entry_duracion.insert(0, self.duracion_pelicula)
            self.entry_genero.insert(0, self.genero_pelicula)
        except:
            pass        
        
    def eliminar_datos(self):
        
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.id_pelicula)
            #Cargamos de nuevo la tabla para que se acutalice el registro
            self.tabla_peliculas()
            self.id_pelicula = None
        except:
            titulo = 'Eliminar Registro'
            mensaje = 'Error al eliminar registro'
            messagebox.showerror(titulo, mensaje)
        