from tkinter import *

menu_inicial = Tk()
menu_inicial.title("TEXTOOO")
menu_inicial.geometry("500x500")

texto = StringVar() #variavel para inserir nas label
texto.set("makunouchi")# maneira para setar variaveis em label

label1 = Label(

bg="blue",
font="arial 20",
textvariable=texto 



).pack()








menu_inicial.mainloop()