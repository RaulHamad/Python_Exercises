from tkinter import *

root = Tk()
root.title("Login")

def executando():
    l1["text"] = e1.get()


# ------------Widgets--------------
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
l1 = Label(root)
l2 = Label(root)
l3 = Label(root)
b = Button(root,text="executar",command=executando)

# ------- LAYOUT-----------
e1.grid()
e2.grid()
e3.grid()
l1.grid()
l1.grid()
l1.grid()
b.grid()


root.mainloop()