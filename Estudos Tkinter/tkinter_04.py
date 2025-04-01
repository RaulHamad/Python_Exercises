#fontes 
from tkinter import *

root = Tk()
root.title("titulooo")
root.geometry("500x500")

#bg = background
#fg = cor da fonte
#width = largura da label
#height = altura da label
#anchor = alinhamento do texto na label
# bd ou borderwidth = modelos de borda para label
#padx = espaço horizontal que o label fica perante o texto
#pady = espaço vertical que o label fica perante o texto
#justify = justifica o texto mas nao alinha




label_1= Label(root,text="testando label 1",
 bg="silver", font="times 20 bold", fg="red",
 width=20,height=2,anchor="w")#width eh tamanho da label
label_1.pack()

label_2 = Label(text="frase 1",bg="blue",font="arial 20",borderwidth=10, relief="solid")

label_2.pack()
label_3 = Label(text="frase 1\n eaeeeeeeee",bg="red",font="arial 20",borderwidth=1, relief="flat",padx=10,pady=15,justify=CENTER)

label_3.pack()
label_4 = Label(text="frase 1",font="arial 20",borderwidth=5, relief="groove")

label_4.pack()
label_5 = Label(text="frase 1",font="arial 20",borderwidth=5, relief="raised")

label_5.pack()
label_6 = Label(text="frase 1",font="arial 20",borderwidth=5, relief="ridge")

label_6.pack()
label_7 = Label(text="frase 1",font="arial 20",borderwidth=5, relief="sunken")

label_7.pack()

root.mainloop()