#posicao do formulario
#from tkinter import *

#root = Tk()

#dimensoes
#dimensao da janela 
#largura = 500
#altura = 500
#calculo dimensao do monitor
#largura_screen = root.winfo_screenwidth()
#altura_screen = root.winfo_screenheight()

#print(largura_screen)
##print(altura_screen)

#calculo para posicionamento da janela
#pos_x = (largura_screen/2) - (largura/2)
#pos_y = (altura_screen/2) - (altura/2)

#root.geometry("%dx%d+%d+%d" % (largura,altura,pos_x,pos_y))



#root.mainloop()

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont

# Função para carregar e mostrar a imagem de fundo
def carregar_imagem():
    caminho_imagem = filedialog.askopenfilename(title="Selecione uma imagem", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if caminho_imagem:
        imagem_fundo = Image.open(caminho_imagem)
        imagem_fundo.thumbnail((500, 500))  # Redimensiona para exibir na interface
        imagem_fundo_tk = ImageTk.PhotoImage(imagem_fundo)
        canvas.create_image(0, 0, anchor=tk.NW, image=imagem_fundo_tk)
        canvas.imagem_fundo = imagem_fundo  # Mantém a referência da imagem para evitar que seja coletada pelo garbage collector

# Função para adicionar os dados na imagem
def adicionar_dados():
    if not hasattr(canvas, 'imagem_fundo'):
        messagebox.showerror("Erro", "Nenhuma imagem carregada!")
        return

    imagem_fundo = canvas.imagem_fundo.copy()
    draw = ImageDraw.Draw(imagem_fundo)

    # Usar uma fonte padrão
    fonte = ImageFont.load_default()

    # Adiciona os dados na imagem
    draw.text((50, 50), f"Nome: {nome_entry.get()}", font=fonte, fill="black")
    draw.text((50, 100), f"Telefone: {telefone_entry.get()}", font=fonte, fill="black")
    draw.text((50, 150), f"Email: {email_entry.get()}", font=fonte, fill="black")

    # Exibir a imagem resultante
    imagem_fundo.show()

    # Opcional: Salvar imagem gerada
    caminho_salvar = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")])
    if caminho_salvar:
        imagem_fundo.save(caminho_salvar)
        messagebox.showinfo("Sucesso", "Imagem salva com sucesso!")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Gerador de Cartão")

# Canvas para exibir a imagem
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Botão para carregar a imagem
carregar_button = tk.Button(root, text="Carregar Imagem", command=carregar_imagem)
carregar_button.pack()

# Campos de entrada para dados
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Nome:").grid(row=0, column=0)
nome_entry = tk.Entry(frame)
nome_entry.grid(row=0, column=1)

tk.Label(frame, text="Telefone:").grid(row=1, column=0)
telefone_entry = tk.Entry(frame)
telefone_entry.grid(row=1, column=1)

tk.Label(frame, text="Email:").grid(row=2, column=0)
email_entry = tk.Entry(frame)
email_entry.grid(row=2, column=1)

# Botão para adicionar dados na imagem
adicionar_button = tk.Button(root, text="Adicionar Dados", command=adicionar_dados)
adicionar_button.pack(pady=10)

root.mainloop()