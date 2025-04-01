from tkinter import *

root = Tk()
root.geometry("300x300")





meu_menu = Menu(root)

# MENU menu
fileMenu = Menu(meu_menu, tearoff=0)#tearoff tira marca que separa as opçoes dentro do menu
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=root.destroy)#destroy fecha a janela

meu_menu.add_cascade(label="File",menu=fileMenu)
# MENU edit-------------------
editMenu = Menu(meu_menu, tearoff=0)#tearoff tira marca que separa as opçoes dentro do menu
editMenu.add_command(label="copy")
editMenu.add_command(label="paste")
editMenu.add_command(label="select all")

meu_menu.add_cascade(label="Edit",menu=editMenu)
botao = Button(root,text="Testes")
botao.config(width=10,font=("calibri",20,"bold"), bg="#158645",fg="#DAD5D6",cursor="hand2",
             activebackground="blue")
botao.grid(padx=20,pady=20)


root.config(menu=meu_menu)
root.mainloop()