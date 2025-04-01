from tkinter import *
# CRIANDO FRAMES
root = Tk()
root.title("app")

frame_name = Frame(root)
frame_rua = Frame(root)


nome = Label(frame_name,text="Nome:")
apelido = Label(frame_name,text="Apelido:")
nome_entry = Entry(frame_name, )
apelido_entry = Entry(frame_name)

rua = Label(frame_rua,text="Rua:")
cidade = Label(frame_rua,text="cidade:")
rua_entry = Entry(frame_rua)
cidade_entry = Entry(frame_rua)

btn = Button(root,text="salvar")


#-----------------------------
nome.grid(row=0,column=0)
apelido.grid(row=1,column=0)
nome_entry.grid(row=0,column=1)
apelido_entry.grid(row=1,column=1)

rua.grid(row=0,column=2)
cidade.grid(row=1,column=2)
rua_entry.grid(row=0,column=3)
cidade_entry.grid(row=1,column=3)




frame_name.grid(row=0,column=0)
frame_rua.grid(row=0,column=1)
btn.grid(columnspan=4)





root.mainloop()