#Es nuestro módulo principal del proyecto

import tkinter as tk
#Importamos las clases del módulo gui_app
from client.gui_app import Frame, barra_menu

def main():
    root=tk.Tk()
    root.title('Catálogo de Películas')
    #root.iconbitmap('img/cp-logo.ico')
    root.resizable(0,0)
    
    barra_menu(root)
    
    #Definimos un objeto de la clase Frame
    app = Frame(root =root)
    
    app.mainloop()
    
if __name__ == '__main__':
    main()