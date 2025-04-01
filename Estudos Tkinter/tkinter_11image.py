

#root = Tk()

#img =PhotoImage(file="image/branca.png")

#label_image = Label(root,image=img).pack()

from tkinter import *
import sqlite3
from tkinter import ttk


class Gerenciador():

    

    def __init__(self, root):
        
        #CRIANDO TELA INICIAL DO APP
        self.tela_inicial = root
        self.tela_inicial.config(bg="#e6ffb3")
        #CONFIGURANDO DIMENSÃO E POSIÇÃO
        
        self.tela_inicial.title("Gestor De Condominio")
        self.tela_inicial.iconbitmap("static/img/paisagem-urbana.ico")
        self.label_titulo = Label(self.tela_inicial,text="APP CONDOMINIO",padx=20,pady=10,font=("times",20,"bold"),borderwidth=2, relief="raised")
        self.label_titulo.grid(row=0,columnspan=2)
        #CRIANDO FRAME PARA LOGIN
        
        #inserindo imagem tela login
        foto_login = PhotoImage(file="static\img\condominio.png")
        self.add_imagem = Label(image= foto_login)
        self.add_imagem.grid()

#root.mainloop()










if __name__ == "__main__":
    root = Tk()
    app = Gerenciador(root)

    root.mainloop()


