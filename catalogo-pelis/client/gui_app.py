import tkinter as tk

def barra_menu(root):
    #Definimos el objeto barra_menu
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width=300, height=300)
    
    #Agregamos menú Inicio a la barra de menú
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    
    #Se ancla al menú inicio
    barra_menu.add_cascade(label = 'Inicio', menu = menu_inicio)
    #Agregamos los submenú del menú Inicio
    menu_inicio.add_cascade(label='Crear Registro')
    menu_inicio.add_cascade(label='Eliminar Registro')
    #La opción Salir le agregamos el evento destroy para cerrar la ventana
    menu_inicio.add_cascade(label='Salir', command =root.destroy)
    
    #Agregamos a la barra de menú otras opciones
    barra_menu.add_cascade(label = 'Consultas')
    barra_menu.add_cascade(label = 'Configuración')
    barra_menu.add_cascade(label = 'Ayuda')

#Definimos la clase padre
class Frame(tk.Frame):
    #Definimos el constructor que recibe la raíz o ventana
    def __init__(self, root = None):
        #Usamos la función super() para heredar el constructor de la clase padre
        super().__init__(root, width=480, height=320)
        self.root = root
        #Empaquetamos
        self.pack()
        #self.config(bg='blue')
        
        self.campos_pelis()
        
    def campos_pelis(self):
        #Definimos las etiquetas Nombre, Duración y Género
        self.label_nombre = tk.Label(self, text = 'Nombre: ')
        self.label_nombre.config(font = ('Carlito', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx =10, pady =10)
        
        self.label_nombre = tk.Label(self, text = 'Duración: ')
        self.label_nombre.config(font = ('Carlito', 12, 'bold'))
        self.label_nombre.grid(row=1, column=0, padx =10, pady =10)
        
        self.label_nombre = tk.Label(self, text = 'Género: ')
        self.label_nombre.config(font = ('Carlito', 12, 'bold'))
        self.label_nombre.grid(row=2, column=0, padx =10, pady =10)
        
        #Definimos los cuadro de textos para cada uno de los campos
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.config(width=50, state='disable', font=('Carlito', 12))
        self.entry_nombre.grid(row=0, column=1, padx =10, pady =10)
        
        self.entry_duracion = tk.Entry(self)
        self.entry_duracion.config(width=50, state='disable', font=('Carlito', 12))
        self.entry_duracion.grid(row=1, column=1, padx =10, pady =10)
        
        self.entry_genero = tk.Entry(self)
        self.entry_genero.config(width=50, state='disable', font=('Carlito', 12))
        self.entry_genero.grid(row=2, column=1, padx =10, pady =10)