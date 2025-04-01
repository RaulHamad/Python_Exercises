from tkinter import *

# CRIANDO classe


class NewFrame(Frame):
    def __init__(self,parent):
        super().__init__()

        self["bd"]=1
        self["relief"]=SOLID

               
        self.text_label = StringVar()
        self.text_entry = StringVar()

        #widget
        self.label_1 =Label(self,textvariable=self.text_label).grid()
        text1 = Entry(self,textvariable=self.text_entry).grid()
        btn = Button(self,text="clique",command=self.Executar,font=("calibri",15,"bold")).grid()

    def Executar(self):
        self.text_label.set(f'Olá {self.text_entry.get()}.')

   


root = Tk()
root.title("app")
root.geometry("300x300")
fr1 = NewFrame(root).grid(column=0)
fr2 = NewFrame(root).grid(row=0,column=1)

root.mainloop()