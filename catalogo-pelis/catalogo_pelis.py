#!/usr/bin/env python3
#coding=utf-8

#Es nuestro módulo principal que contendra el entrypoint y la función principal
#Importamos la librería tkinder con el alias tk
import tkinter as tk
#Importamos las clases del módulo gui_app
from client.gui_app import Frame, barra_menu

#Definimos la función principal main()
def main():
    root=tk.Tk()
    root.title('Catálogo de Películas en Python')
    #root.iconbitmap('img/cp-logo.ico')
    #Para que las dimensiones de la ventana no sea modificable
    root.resizable(0,0)
    
    barra_menu(root)
    
    #Definimos un objeto de la clase Frame (contenedor para formularios)
    app = Frame(root =root)
    #Indica el final de la ejecución de nuestra aplicación
    app.mainloop()

#Definimos el entrypoint
if __name__ == '__main__':
    main()