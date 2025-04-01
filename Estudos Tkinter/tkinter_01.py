"""from tkinter import *

root = Tk()

root.title("ola como vai tuo bem")
root.geometry("500x500+200+200")# tamanho da janela e lugar onde surgi a janela
root.resizable(True,True)#booleano e pode aumentar a largura ou nao da janela
root.minsize(width=500,height=250)#dimensoes minimas iniciais
root.maxsize(800,800)# dimensoes maxima qd maximinizar
root.state("zoomed")#inicializa com janela maximinizada
root.state("iconic")#inicializa com janela minimizada
root.iconbitmap("")# altera icone da janela- especificando caminho
btn = Button(root,text="concluir")# adiciona botao
btn.pack( fill=X)#funcao que confirma o "botao" FILL expande o botao em toda linha
root["bg"] = "blue" # cor de fundo




root.mainloop()

"""

import tkinter as tk
from tkinter import ttk

win = tk.Tk()

v = tk.StringVar()
def setText(word):
    v.set(word)

a = ttk.Button(win, text="plant", command=setText("plant"))
a.pack()
b = ttk.Button(win, text="animal", command=setText("animal"))
b.pack()
c = ttk.Entry(win, textvariable=v)
c.pack()
win.mainloop()