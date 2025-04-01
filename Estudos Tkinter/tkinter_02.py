"""from tkinter import *

root = Tk()
root.title("Titulo")
root["bg"] = "blue"
def btn_Click():
    print("ola mundo")

def btn2_Click(msg):
    print(msg)

btn = Button(root,text="concluir", command=btn_Click) # command éo nome da funcao que deve ser criada antes do botao
#Para criar funcao com argumento eh necessario usar o lambda
btn2 = Button(root,text="funcao lammbda", command=lambda:btn2_Click("mensagem")) # command éo nome da funcao que deve ser criada antes do botao
btn3 = Button(root,text="funcao direta no botao", command=lambda:print("hello world"))
btn3.pack()
btn.pack()
btn2.pack()

#A SEQUENCIA DOS PACK INDICA COMO FICA NA JANELA. BTN, BTN2, BTN3
"""


