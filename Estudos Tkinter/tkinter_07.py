from tkinter import *

root = Tk()
root.title("Login")

def logando():
    label3["text"] = entry_usuario.get()




label1 = Label(root, text="Usuario:",font="times 10").grid(row=0,sticky=W)
label2 = Label(root, text="Senha:",font="times 10").grid(row=1,sticky=W)
entry_usuario = Entry(root)
entry_senha = Entry(root)

btn = Button(root,text="Login",command=logando).grid(row=2,column=1,stick=E)
entry_usuario.grid(row=0,column=1)
entry_senha.grid(row=1,column=1)
label3 = Label(root)
label3.grid(columnspan=2,sticky="we")
# primeiro cria a entry, depois grid, depois focus
entry_usuario.focus() # inicia com o curso do mouse para digitar nessa entry


root.mainloop()