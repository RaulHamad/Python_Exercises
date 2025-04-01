from tkinter import *

menu_inicial = Tk()
menu_inicial.title("TEXTOOO")
#menu_inicial.geometry("500x500")


label1 = Label(menu_inicial, text="label1",font="arial 20",bg="blue")
label2 = Label(menu_inicial, text="label1",font="arial 20",bg="red")
label3 = Label(menu_inicial, text="label1",font="arial 20",bg="green")

#columnspan aumenta o grid junto com sticky
label4 = Label(menu_inicial, text="label4",font="arial 20",bg="purple").grid(row=4,columnspan=3, sticky="we")

btn = Button(menu_inicial,text="click1",font="arial 10")
btn2 = Button(menu_inicial,text="click2",font="arial 10")
btn3 = Button(menu_inicial,text="click3",font="arial 10")




label1.grid(row=0,column=0)
label2.grid(row=1,column=1)
label3.grid(row=2,column=2)
btn.grid(row=1,column=0)
btn2.grid(row=2,column=1)
btn3.grid(row=3,column=2)


menu_inicial.mainloop()