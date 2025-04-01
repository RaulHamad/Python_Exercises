from tkinter import *

root = Tk()
root.title("Conversor")
#root.geometry("400x400")

frame_converter = Frame(root)



final = StringVar()

# (0 °C × 9/5) + 32
def converter():
    celsius = float(entrada_Celsius.get())
    faren = (celsius * (9/5)) + 32
    final.set(str(faren)+ " graus faren")
    label_final= Label(frame_converter,textvariable=final)
    label_final.grid(columnspan=2)
    
#widgets frame 1
label_1 = Label(frame_converter,text="Conversor de temperatura",font="arial 15",border=1,relief="sunken")
text_Celsius = Label(frame_converter,text="Temperatura em Cº:",font="arial 10",anchor="e",width=15)
entrada_Celsius = Entry(frame_converter)
conversor = Button(frame_converter,text="Converter", command=converter)



# layout frame 1

label_1.grid(row=0,columnspan=2)
text_Celsius.grid(row=1,column=0,sticky="e")
entrada_Celsius.grid(row=1,column=1)
conversor.grid(row=2,column=1)

entrada_Celsius.focus()



frame_converter.grid()

root.mainloop()