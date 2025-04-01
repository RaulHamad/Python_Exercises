from tkinter import *
# CRIANDO FRAMES
root = Tk()
root.title("app")

def apresentar():
    print(valor_check.get())

# criando checkbox

valor_check = BooleanVar()
checkbox = Checkbutton(root,text="opção ao lado",variable=valor_check,command=apresentar).pack( )

#Criando radio button
var_1 = IntVar()
ra_1 = Radiobutton(root,text="opcao 1",variable=var_1,value=1,command=apresentar)
ra_2 = Radiobutton(root,text="opcao 2",variable=var_1,value=2)
ra_3 = Radiobutton(root,text="opcao 3",variable=var_1,value=3)

ra_1.pack()
ra_2.pack()
ra_3.pack()
ra_1.select() # iniciar com uma selecao



list_box = Listbox(root,selectmode=EXTENDED)#selectmode para selecionar mais de um texto da listbox   
list_box.pack()
list_box.insert(END,"primeiro")#insere o indice e o texto String
list_box.insert(END,"segundo")
list_box.insert(0,"terceiro")



root.mainloop()