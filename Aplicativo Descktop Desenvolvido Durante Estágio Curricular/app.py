from import_data_xml import Data
from tk_variables_and_color import Variables_and_colors
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont
import qrcode
from sys import platform
import os
from fpdf import FPDF
import customtkinter as ctk

import win32print
import win32api
import shutil


class App_Card(Data, Variables_and_colors):

    def __init__(self):
        root = ctk.CTk()

        self.root = root
        self.variable()
        self.colors()
        self.init_data_base()
        self.home_config()
        self.download_xml()
        self.filter_members()
        self.frame_home_screen()
        self.generate_all_qrcode()
        self.main_tree_view()

        root.mainloop()

    def home_config(self):
        """
        Inicialização e configuração da janela principal
        """

        self.download_xml()
        self.filter_members()

        self.root.title("Sócios Online - Impressão de cartões")
        self.root.resizable(False, False)
        self.root.configure(bg=self.gray1)

        self.root.iconbitmap(self.resource_path("logo.ico"))
        # self.root.maxsize(650,550)
        # self.root.minsize(500,400)
        # Centralizar o app ao iniciar
        width_screen = self.root.winfo_screenwidth()
        height_screen = self.root.winfo_screenheight()
        pos_x = (width_screen / 2) - (800 / 2)
        pos_y = (height_screen / 2) - (500 / 2)
        self.root.geometry("%dx%d+%d+%d" % (width_screen, height_screen, pos_x, pos_y))
        self.root.geometry("650x550")
        ctk.set_appearance_mode("dark")

        # Criar menu
        self.menu = Menu(self.root, borderwidth=5, relief="ridge")
        self.root.configure(menu=self.menu)
        self.file_menu = Menu(self.menu, tearoff=False, font=("Robot", 10))
        self.file_menu.add_command(
            label="Início", command=self.click_function_main_treeview
        )
        self.menu.add_cascade(label="Opções", menu=self.file_menu)

        self.file_menu.add_command(label="Carta", command=self.create_layout_letter_pdf)
        self.file_menu.add_command(label="Etiqueta", command=self.layout_print_label)
        self.file_menu.add_command(label="Imprimir lote", command=self.print_all_cards)
        self.file_menu.add_command(label="Dados xml", command=self.data_xml_main_frame)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Sair", command=self.root.destroy)

    def frame_home_screen(self):

        # Criar frame para botões da tela inicial
        self.frame_button = ctk.CTkFrame(
            self.root, fg_color=self.gray1, corner_radius=0, border_width=0
        )
        self.frame_button.place(relx=0.17, rely=0.00, relwidth=0.84, relheight=0.08)
        self.button_add_card = ctk.CTkButton(
            self.frame_button,
            # overrelief=RIDGE,
            text="Editar Cartão de Sócio",
            fg_color=self.blue1,
            corner_radius=20,
            command=self.frame_config_card,
            text_color=self.black,
            font=("Robot", 12),
        )
        self.button_add_card.place(relx=0.05, rely=0.15, relwidth=0.3)

        self.entry_search = ctk.CTkEntry(
            self.frame_button,
            justify=LEFT,
            text_color=self.black,
            fg_color=self.white,
            # placeholder_text= self.black
        )
        self.entry_search.insert(
            0, "Pesquisar..."
        )  # Define o texto inicial (placeholder)
        self.entry_search.bind(
            "<FocusIn>", self.focus_in_entry_search
        )  # Remove o placeholder ao clicar
        self.entry_search.bind(
            "<FocusOut>", self.focus_out_entry_search
        )  # Adiciona o placeholder ao sair do foco
        self.entry_search.bind(
            "<Return>", self.search_tree_view
        )  # Busca ao pressionar Enter
        self.entry_search.bind(
            "<KeyRelease>", self.search_tree_view
        )  # busca em tempo real
        self.entry_search.place(relx=0.70, rely=0.18, relwidth=0.25, relheight=0.7)
        # Criar linha de separação
        self.line_separator = ttk.Separator(
            self.frame_button, orient="horizontal", style="TSeparator"
        )
        style = ttk.Style()
        style.configure("TSeparator", background="black")
        self.line_separator.place(relx=0.00, rely=0.92, relwidth=0.99)

    def focus_in_entry_search(self, event):
        if self.entry_search.get() == "Pesquisar...":
            self.entry_search.delete(0, END)
            self.entry_search.configure(fg_color=self.white)

    def focus_out_entry_search(self, event):
        if self.entry_search.get() == "":
            self.entry_search.insert(0, "Pesquisar...")
            self.entry_search.configure(fg_color=self.gray2)
            self.click_function_main_treeview()
        else:
            self.entry_search.delete(0, END)
            self.click_function_main_treeview()

    def search_tree_view(self, event):
        """Realiza a busca na Treeview."""
        # Obtém o texto do campo de busca
        query = self.entry_search.get().lower()

        self.filtered_names = []
        for (
            members
        ) in self.copy_data:  # self.copy_data é variavel que copia os dados dos socios

            # Verifica se o texto buscado está presente no nome (ou outros campos, se necessário)
            if (
                query in members[1].lower()
            ):  # Garante que a comparação seja em minúsculas
                self.filtered_names.append(members)

            # Remove todos os itens existentes na Treeview
        for item in self.check_data.get_children():
            self.check_data.delete(item)

        # Adiciona os itens filtrados (ou nenhum, se a lista estiver vazia)
        if self.filtered_names:
            for index, name in enumerate(self.filtered_names):
                tag = "even" if index % 2 == 0 else "odd"
                self.check_data.insert("", "end", values=(name[0], name[1]), tags=(tag))
        else:
            # Exibe uma mensagem padrão se nenhum nome for encontrado
            self.check_data.insert("", "end", values=("", ""))

    def main_tree_view(self):
        """self.data_client.clear: Apagar variavel com dados de cliente selecionado em caso de retornar
        a tela inical para selecionar outro cliente"""
        self.data_client.clear()
        self.frame_home_screen()

        # criando o objeto para personalizar a treeview
        mystyle = ttk.Style()
        mystyle.theme_use("clam")

        # Configurar o estilo da Treeview
        mystyle.configure(
            "Custom.Treeview",  # Nome do estilo
            background=self.gray1,
            foreground=self.black,
            rowheight=25,
            fieldbackground=self.white,
            borderwidth=1,
        )

        # Configurar o estilo para o cabeçalho da Treeview
        mystyle.configure(
            "Custom.Treeview.Heading",
            background="##F2F2F2",
            foreground=self.black,
            font=("Robot", 10, "bold"),
        )
        mystyle.map("Custom.Treeview", background=[("selected", self.blue1)])
        # Frame para visualização da treeview
        self.frame_treeview = ctk.CTkFrame(
            self.root, fg_color=self.gray1, corner_radius=0, border_width=0
        )
        self.frame_treeview.place(relx=0.17, rely=0.075, relwidth=6.68, relheight=1)
        # Criar a tree view
        self.check_data = ttk.Treeview(
            self.frame_treeview,
            height=1,
            style="Custom.Treeview",
            columns=("col1", "col2"),
            show="headings",
            selectmode="extended",
        )
        self.check_data.tag_configure("odd", background=self.white)
        self.check_data.tag_configure("even", background=self.gray1)

        self.check_data.place(relx=0.003, rely=0.01, relwidth=0.113, relheight=0.9)
        # #configurando titulos

        self.check_data.heading("#1", text="Sócio-Number", anchor=CENTER)
        self.check_data.heading(
            "#2",
            text="Name",
            anchor=CENTER,
        )
        # configurando espaçamento das colunas

        self.check_data.column("#1", width=100, anchor=CENTER)
        self.check_data.column("#2", width=390, anchor=CENTER)
        # adicionando barra de rolagem
        self.scrool = Scrollbar(
            self.frame_treeview, orient="vertical", command=self.check_data.yview
        )
        self.check_data.configure(yscrollcommand=self.scrool.set)

        self.scrool.place(relx=0.117, rely=0.01, relwidth=0.004, relheight=0.9)
        # atualiza os dados da treeview
        self.check_data.delete(*self.check_data.get_children())
        # inserir dados na treeview
        for index, check_members in enumerate(self.filter_members()):
            tag = "even" if index % 2 == 0 else "odd"
            self.check_data.insert(
                "", END, values=(check_members[0], check_members[3]), tags=(tag)
            )

        self.check_data.bind("<Double-1>", self.double_click_frame_config_card)
        # frame para os botoes do menu a esquerda
        self.menu_button_frame = ctk.CTkFrame(
            self.root, fg_color=self.gray1, corner_radius=0, border_width=1
        )
        self.menu_button_frame.place(relx=0.0, rely=0.0, relwidth=0.17, relheight=1)

        self.letter_photo = Image.open(self.resource_path("carta.png"))

        self.letter_photo = ctk.CTkImage(
            light_image=self.letter_photo, dark_image=self.letter_photo, size=(50, 50)
        )
        self.button_letter = ctk.CTkButton(
            self.menu_button_frame,
            fg_color=self.blue1,
            text_color=self.black,
            corner_radius=30,
            command=self.create_layout_letter_pdf,
            image=self.letter_photo,
            text="Imprimir\n Carta",
            compound="top",
        )
        self.button_letter.place(relx=0.05, rely=0.015, relwidth=0.91, relheight=0.17)

        self.labell_photo = Image.open(self.resource_path("etiqueta.png"))

        self.labell_photo = ctk.CTkImage(
            light_image=self.labell_photo, dark_image=self.labell_photo, size=(50, 50)
        )

        self.button_label = ctk.CTkButton(
            self.menu_button_frame,
            fg_color=self.blue1,
            text_color=self.black,
            corner_radius=30,
            command=self.layout_print_label,
            image=self.labell_photo,
            text="Imprimir\n Etiqueta",
            compound="top",
        )
        self.button_label.place(relx=0.05, rely=0.215, relwidth=0.91, relheight=0.17)

        self.printer_photo = Image.open(self.resource_path("impressora.png"))

        self.printer_photo = ctk.CTkImage(
            light_image=self.printer_photo, dark_image=self.printer_photo, size=(50, 50)
        )

        self.button_print_card = ctk.CTkButton(
            self.menu_button_frame,
            fg_color=self.blue1,
            text_color=self.black,
            corner_radius=30,
            command=self.print_selected_card,
            image=self.printer_photo,
            text="Imprimir\nCartão",
            compound="top",
        )
        self.button_print_card.place(
            relx=0.05, rely=0.415, relwidth=0.91, relheight=0.17
        )

        self.button_print_all_card = ctk.CTkButton(
            self.menu_button_frame,
            fg_color=self.blue1,
            text_color=self.black,
            corner_radius=30,
            command=self.print_all_cards,
            image=self.printer_photo,
            text="Imprimir\nLote",
            compound="top",
        )
        self.button_print_all_card.place(
            relx=0.05, rely=0.615, relwidth=0.91, relheight=0.17
        )

        self.xml_photo = Image.open(self.resource_path("xml.png"))

        self.xml_photo = ctk.CTkImage(
            light_image=self.xml_photo, dark_image=self.xml_photo, size=(50, 50)
        )

        self.button_label = ctk.CTkButton(
            self.menu_button_frame,
            fg_color=self.blue1,
            text_color=self.black,
            corner_radius=30,
            command=self.data_xml_main_frame,
            image=self.xml_photo,
            text="Link\nXml",
            compound="top",
        )
        self.button_label.place(relx=0.05, rely=0.815, relwidth=0.91, relheight=0.17)

    def create_layout_letter_pdf(self):
        """
        função que cria o layout para criação da carta.
        :return: imprimir carta ou etiqueta em lote
        """
        try:
            self.button_print_card.destroy()
            self.button_add_card.destroy()
            self.entry_search.destroy()
        except:
            pass

        self.frame_letter = Frame(self.root, background=self.gray1)
        self.frame_letter.place(relx=0.00, rely=0.00, relwidth=1, relheight=1)

        self.laber_sender = Label(
            self.frame_letter,
            text="Remetente ",
            fg=self.black,
            bg=self.gray1,
            font=("Robot", 14),
            anchor="center",
            relief="sunken",
            borderwidth=2,
        )
        self.laber_sender.place(relx=0.02, rely=0.02, relwidth=0.95, relheight=0.05)

        self.laber_sender_name = Label(
            self.frame_letter,
            text="Nome: ",
            fg=self.black,
            bg=self.gray1,
            font=("Robot", 10),
            anchor="w",
        )
        self.laber_sender_name.place(relx=0.02, rely=0.1, relwidth=0.1, relheight=0.02)

        self.entry_sender_name = Entry(
            self.frame_letter,
            # textvariable=self.open_photo,
            justify=LEFT,
            font=("Robot", 12),
            # state="readonly",
        )
        self.entry_sender_name.place(
            relx=0.02, rely=0.13, relwidth=0.95, relheight=0.04
        )

        self.laber_sender_address = Label(
            self.frame_letter,
            text="Morada: ",
            fg=self.black,
            bg=self.gray1,
            font=("Robot", 10),
            anchor="w",
        )
        self.laber_sender_address.place(
            relx=0.02, rely=0.20, relwidth=0.1, relheight=0.02
        )

        self.entry_sender_address = Entry(
            self.frame_letter,
            # textvariable=self.open_photo,
            justify=LEFT,
            font=("Robot", 12),
            # state="readonly",
        )
        self.entry_sender_address.place(
            relx=0.02, rely=0.23, relwidth=0.95, relheight=0.04
        )

        self.laber_message = Label(
            self.frame_letter,
            text="Mensagem: ",
            fg=self.black,
            bg=self.gray1,
            font=("Robot", 12),
            anchor="w",
        )
        self.laber_message.place(relx=0.02, rely=0.35, relwidth=0.15, relheight=0.05)

        self.text_message = Text(self.frame_letter)
        self.text_message.place(relx=0.02, rely=0.4, relwidth=0.93, relheight=0.5)

        scrollbar_message = Scrollbar(
            self.frame_letter, command=self.text_message.yview
        )
        self.text_message.config(yscrollcommand=scrollbar_message.set)
        scrollbar_message.place(relx=0.95, rely=0.4, relwidth=0.02, relheight=0.5)
        self.text_message.insert(1.3, "Digite sua mensagem...")
        self.text_message.bind("<FocusIn>", self.focus_in_entry_text)

        self.button_erase_text = ctk.CTkButton(
            self.frame_letter,
            text="Limpar",
            text_color=self.black,
            fg_color=self.blue1,
            corner_radius=20,
            command=self.text_message_clear,
        )
        self.button_erase_text.place(relx=0.02, rely=0.91, relwidth=0.15)

        self.button_print_text = ctk.CTkButton(
            self.frame_letter,
            text="Imprimir",
            text_color=self.black,
            fg_color=self.blue1,
            corner_radius=20,
            command=self.print_pdf_letter,
        )
        self.button_print_text.place(relx=0.82, rely=0.91, relwidth=0.15)

    def focus_in_entry_text(self, event):
        if self.text_message.get("1.0", "end-1c") == "Digite sua mensagem...":
            self.text_message.delete("1.0", "end")

    def text_message_clear(self):
        self.text_message.delete("1.0", "end")

    def print_pdf_label(self):
        """
        Gera um único PDF com as etiquetas para impressão.
        """

        pdf_label = FPDF(
            unit="mm",
            format=(
                float(self.width_label_entry.get()),
                float(self.height_label_entry.get()),
            ),
        )

        for index, label in enumerate(self.list_dict):

            try:
                pdf_label.add_page()
                pdf_label.set_fill_color(
                    self.background_label_letter_rgb[0],
                    self.background_label_letter_rgb[1],
                    self.background_label_letter_rgb[2],
                )

                pdf_label.set_text_color(
                    self.color_label_letter_rgb[0],
                    self.color_label_letter_rgb[1],
                    self.color_label_letter_rgb[2],
                )
                pdf_label.set_font("Arial", size=self.size_text_label.get())

                pdf_label.multi_cell(
                    (self.width_label_entry.get() - 10),
                    (self.height_label_entry.get() / 4),
                    f"{label[3]} - {label[6]}, {label[7]}",
                    fill=True,
                    align="C",
                )

                os.makedirs("pdf_etiquetas", exist_ok=True)
                self.pdf_label_path = os.path.abspath("pdf_etiquetas/etiquetas.pdf")

            except:
                print("error etiqueta")

        pdf_label.output(self.pdf_label_path)
        self.check_print_labels = "label"
        self.screen_printer()

    def print_pdf_letter(self):
        """
        Gera um único PDF com as etiquetas para impressão.
        """

        pdf_letter = FPDF(unit="mm", format="A4")
        pdf_letter.set_font("Arial", size=12)
        for index, letter in enumerate(self.list_dict):

            try:

                # Adicionar Remetente
                pdf_letter.add_page()
                pdf_letter.set_font("Arial", "B", size=14)
                pdf_letter.cell(0, 10, self.entry_sender_name.get(), ln=True)
                pdf_letter.set_font("Arial", size=10)
                pdf_letter.cell(0, 0, self.entry_sender_address.get(), ln=True)
                pdf_letter.ln(30)

                pdf_letter.set_font("Arial", size=14)
                pdf_letter.cell(0, 10, f"Destinatário:", ln=True)
                pdf_letter.set_font("Arial", "B", size=14)
                pdf_letter.cell(0, 10, letter[3], ln=True)
                pdf_letter.set_font("Arial", size=10)
                pdf_letter.cell(0, 0, f"{letter[6]}, {letter[7]}", ln=True)
                pdf_letter.ln(30)

                pdf_letter.set_font("Arial", size=12)
                pdf_letter.cell(0, 10, "Caro(a) associado(a),", ln=True)
                pdf_letter.set_font("Arial", size=10)
                pdf_letter.multi_cell(0, 10, self.text_message.get("1.0", "end-1c"))
                pdf_letter.ln(30)

                pdf_letter.set_font("Arial", size=10)
                pdf_letter.cell(0, 10, "Atenciosamente,", ln=True)
                pdf_letter.cell(0, 10, self.entry_sender_name.get(), ln=True)

                os.makedirs("pdf_carta", exist_ok=True)
                self.pdf_letter_path = os.path.abspath("pdf_carta/cartas.pdf")

            except:
                print("error carta")
        pdf_letter.output(self.pdf_letter_path)
        # variavel que se for igual a "label", imprime etiquetas. se for igual a "letter" imprime carta.Se for '' imprimi cartão
        self.check_print_labels = "letter"
        self.screen_printer()

    def click_function_main_treeview(self):
        """
        Função para evitar que se gere várias treeview uma por cima da outra
        Apaga listas de seleção
        Encerra janelas top level
        """

        self.values = []
        self.data_client = []
        self.frame_treeview.destroy()
        self.check_print_labels = ""
        try:
            self.frame_letter.destroy()
        except:
            pass
        self.main_tree_view()
        self.check_data.selection_clear()
        try:
            self.window_printer.destroy()
        except:
            print("janela printer não foi aberta")
        try:
            self.window_xml.destroy()
        except:
            print("janela  xml não foi aberta")
        try:
            self.window_ticket.destroy()
        except:
            print("janela  etiqueta não foi aberta")

    def generate_all_qrcode(self):
        """
        Criar todas os Qrcodes de cada cliente
        """

        for clients in self.list_dict:

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(clients[9])
            qr.make(fit=True)

            self.create_image = qr.make_image(fill_color="black")
            os.makedirs("image_qrcode", exist_ok=True)
            path_qrcode = os.path.abspath(
                os.path.join(
                    "image_qrcode",
                    f"{clients[0]}_{clients[3].replace(' ', '_')}_QrCode.png",
                )
            )
            if not os.path.exists(path_qrcode):

                # Salvar imagem do qrcode
                self.create_image.save(path_qrcode)
                # salvar caminho no banco de dados
                self.open_sql()
                client_and_qrcode = "INSERT INTO Socios (number,name, qrcode,email,phone,address,postal_code,country) VALUES (?,?,?,?,?,?,?,?)"
                self.cursor.execute(
                    client_and_qrcode,
                    (
                        clients[0],
                        clients[3],
                        path_qrcode,
                        clients[4],
                        clients[5],
                        clients[6],
                        clients[7],
                        clients[8],
                    ),
                )
                self.close_sql()

            else:
                print("qrcode ja está salvo")

    def print_all_cards(self):

        # variavel para ativar a impressao de etiquetas
        self.check_print_labels = ""
        # apagar lista com os caminhos salvos para imprimir
        self.list_cards_for_printer = []

        # posição do nome,número e qrcode do sócio
        self.namex_entry.set(50)
        self.namey_entry.set(215)
        self.name_size_entry.set(15)
        self.numberx_entry.set(335)
        self.numbery_entry.set(135)
        self.number_size_entry.set(20)
        self.qrcodex_entry.set(287)
        self.qrcodey_entry.set(25)
        self.qrcode_entry_size_x.set(105)
        self.qrcode_entry_size_y.set(103)

        for clients in self.list_dict:

            os.makedirs("image_card_base", exist_ok=True)
            os.makedirs("image_card", exist_ok=True)
            shutil.copy(
                self.resource_path("model_card.png"),
                os.path.abspath(os.path.join("image_card_base")),
            )
            self.image_base = os.path.abspath(
                os.path.join("image_card_base", "model_card.png")
            )

            with Image.open(self.image_base) as self.img:
                self.img = self.img.resize((420, 265))
                self.path_img = self.img
            self.draw = ImageDraw.Draw(self.img)
            entries = [
                int(self.name_size_entry.get()),
                int(self.number_size_entry.get()),
                int(self.qrcode_entry_size_x.get()),
                int(self.qrcode_entry_size_y.get()),
            ]

            # Verificação simplificada

            if all(value > 0 for value in entries):
                self.draw.text(
                    (self.namex_entry.get(), self.namey_entry.get()),
                    clients[3],
                    fill=self.black,
                    font=ImageFont.truetype("arial.ttf", self.name_size_entry.get()),
                    encoding="utf-8",
                )
                self.draw.text(
                    (self.numberx_entry.get(), self.numbery_entry.get()),
                    clients[0],
                    fill=self.white,
                    font_size=self.number_size_entry.get(),
                )
                for query_number in self.query_data_card():

                    if str(query_number[1]) == clients[0]:
                        self.path_qrcode = Image.open(query_number[3])

                        self.path_qrcode = self.path_qrcode.resize(
                            (
                                self.qrcode_entry_size_x.get(),
                                self.qrcode_entry_size_y.get(),
                            )
                        )
                        self.path_img.paste(
                            self.path_qrcode,
                            (self.qrcodex_entry.get(), self.qrcodey_entry.get()),
                        )
                        path_card = os.path.abspath(
                            os.path.join(
                                "image_card",
                                rf"{clients[0]}_{clients[3].replace(' ','')}_card.png",
                            )
                        )
                        self.list_cards_for_printer.append(path_card)
                        if not os.path.exists(path_card):
                            self.path_img.save(path_card)
                            # salvar caminho no banco de dados
                            self.open_sql()
                            card = f"Update Socios SET card =  ? WHERE number = ?"
                            self.cursor.execute(card, (path_card, clients[0]))
                            self.close_sql()
        self.screen_printer()

    def print_selected_card(self):
        """
        Função para imprimir apenas os sócios selecionados na treeview

        """
        # variavel para ativar a impressao de etiquetas
        self.check_print_labels = ""
        # apagar lista com os caminhos salvos para imprimir
        self.list_cards_for_printer = []

        # Verificar se algum sócio foi selecionado
        self.select_names = self.check_data.selection()

        if not self.check_data.selection():
            messagebox.showwarning("Aviso", "Por favor, selecione um item da lista.")
            return self.click_function_main_treeview()
        # Variável que armazena o número e nome do cliente selecionado
        for item in self.select_names:
            item_value = self.check_data.item(item, "values")
            self.values.append(item_value)
        print(self.values)

        # posição do nome,número e qrcode do sócio
        self.namex_entry.set(50)
        self.namey_entry.set(215)
        self.name_size_entry.set(15)
        self.numberx_entry.set(335)
        self.numbery_entry.set(135)
        self.number_size_entry.set(20)
        self.qrcodex_entry.set(287)
        self.qrcodey_entry.set(25)
        self.qrcode_entry_size_x.set(105)
        self.qrcode_entry_size_y.set(103)
        for clients in self.values:

            os.makedirs("image_card_base", exist_ok=True)
            os.makedirs("image_card", exist_ok=True)
            shutil.copy(
                self.resource_path("model_card.png"),
                os.path.abspath(os.path.join("image_card_base")),
            )
            self.image_base = os.path.abspath(
                os.path.join("image_card_base", "model_card.png")
            )

            with Image.open(self.image_base) as self.img:
                self.img = self.img.resize((420, 265))
                self.path_img = self.img
            self.draw = ImageDraw.Draw(self.img)
            entries = [
                int(self.name_size_entry.get()),
                int(self.number_size_entry.get()),
                int(self.qrcode_entry_size_x.get()),
                int(self.qrcode_entry_size_y.get()),
            ]

            # Verificação simplificada

            if all(value > 0 for value in entries):
                self.draw.text(
                    (self.namex_entry.get(), self.namey_entry.get()),
                    clients[1],
                    fill=self.black,
                    font=ImageFont.truetype("arial.ttf", self.name_size_entry.get()),
                    encoding="utf-8",
                )
                self.draw.text(
                    (self.numberx_entry.get(), self.numbery_entry.get()),
                    clients[0],
                    fill=self.white,
                    font_size=self.number_size_entry.get(),
                )
                for query_name in self.query_data_card():
                    if query_name[2] == clients[1]:
                        self.path_qrcode = Image.open(query_name[3])

                        self.path_qrcode = self.path_qrcode.resize(
                            (
                                self.qrcode_entry_size_x.get(),
                                self.qrcode_entry_size_y.get(),
                            )
                        )
                        self.path_img.paste(
                            self.path_qrcode,
                            (self.qrcodex_entry.get(), self.qrcodey_entry.get()),
                        )
                        path_card = os.path.abspath(
                            os.path.join(
                                "image_card",
                                rf"{clients[0]}_{clients[1].replace(' ', '')}_card.png",
                            )
                        )

                        if not os.path.exists(path_card):
                            self.path_img.save(path_card)
                            # salvar caminho no banco de dados
                            self.open_sql()
                            card = f"Update Socios SET card =  ? WHERE number = ?"
                            self.cursor.execute(card, (path_card, clients[0]))
                            self.close_sql()
        # Pesquisa e salva os caminhos das imagens dos socios selecionaos
        query_card = [i for i in self.query_data_card()]
        values_selected = [i for i in self.values]

        for value in values_selected:
            for card in query_card:

                if value[0] == str(card[1]):
                    self.list_cards_for_printer.append(card[4])

        self.screen_printer()

    def double_click_frame_config_card(self, event):
        """
        :param event: função para abrir editor de cartão com duplo click

        """
        self.frame_config_card()

    def frame_config_card(self):

        # apagar lista com os caminhos salvos para imprimir
        self.list_cards_for_printer = []
        # armazenar todos os dados dos socios selecionados para trabalhar os caminhos de qrcode nome e numero
        self.data_selected_clients = []

        # Verificar se algum sócio foi selecionado
        self.select_names = self.check_data.selection()
        # condicional para abrir o editor se apenas um socio for selecionado na treview
        if not self.check_data.selection() or len(self.select_names) > 1:
            messagebox.showwarning(
                "Aviso", "Por favor, selecione apenas um item da lista."
            )
            return self.click_function_main_treeview()
        # Variável que armazena o número e nome do cliente selecionado
        for item in self.select_names:
            item_value = self.check_data.item(item, "values")
            self.values.append(item_value)

        # Verificar o cliente selecionado na treeview e armazenar todos seus dados na variavel self.list_cards_for_printer
        # Pesquisa e salva os caminhos das imagens dos socios selecionaos
        query_card = [i for i in self.query_data_card()]
        values_selected = [i for i in self.values]
        for value in values_selected:
            for card in query_card:
                if value[1] == card[2]:
                    self.list_cards_for_printer.append(card[4])
                    self.data_selected_clients.append(card)

        # Apaga o frame contendo a treeview
        self.frame_treeview.destroy()

        # frame principal com toda area da janela

        self.frame_main = ctk.CTkFrame(self.root, fg_color=self.gray1)
        self.frame_main.place(relx=0.00, rely=0.00, relwidth=1, relheight=1)
        # Criar Widgets para area de inserir imagem
        self.frame_download_image = ctk.CTkFrame(self.frame_main, fg_color=self.gray1)
        self.frame_download_image.place(
            relx=0.00, rely=0.00, relwidth=1, relheight=0.12
        )
        self.button_download = ctk.CTkButton(
            self.frame_download_image,
            command=self.open_image,
            text="Selecionar Foto",
            text_color=self.black,
            fg_color=self.blue1,
            corner_radius=20,
            font=("Robot", 12, "bold"),
        )
        self.button_download.place(relx=0.05, rely=0.29, relwidth=0.2, relheight=0.40)
        self.entry_download = Entry(
            self.frame_download_image,
            textvariable=self.open_photo,
            justify=LEFT,
            state="readonly",
            bg=self.gray2,
        )
        self.entry_download.place(relx=0.27, rely=0.30, relwidth=0.65, relheight=0.30)
        self.line_separator = ttk.Separator(
            self.frame_main, orient="horizontal", style="TSeparator"
        )
        style = ttk.Style()
        style.configure("TSeparator", background="black")
        self.line_separator.place(relx=0.02, rely=0.11, relwidth=0.95)

        # Criar Widgets para area da url do arquivo xml
        self.frame_url_xml = Frame(self.frame_main, background=self.gray1)
        self.frame_url_xml.place(relx=0.00, rely=0.12, relwidth=1, relheight=0.10)
        self.label_url = Label(
            self.frame_url_xml,
            text="Dados dos Sócios: ",
            fg=self.black,
            bg=self.gray1,
            font=("Robot", 10),
            anchor="w",
        )
        self.label_url.place(relx=0.05, rely=0.09, relwidth=0.18, relheight=0.35)
        self.entry_url = Entry(
            self.frame_url_xml,
            justify=LEFT,
            state="readonly",
            bg=self.gray2,
        )
        self.entry_url.place(relx=0.27, rely=0.10, relwidth=0.65, relheight=0.35)
        self.button_url = ctk.CTkButton(
            self.frame_url_xml,
            text="Alterar",
            command=self.entry_new_data_xml,
            text_color=self.black,
            fg_color=self.blue1,
            corner_radius=20,
            font=("Robot", 12, "bold"),
        )
        self.button_url.place(relx=0.05, rely=0.53, relwidth=0.17, relheight=0.40)
        self.line_separator2 = ttk.Separator(
            self.frame_main, orient="horizontal", style="TSeparator"
        )
        style = ttk.Style()
        style.configure("TSeparator", background="black")
        self.line_separator2.place(relx=0.02, rely=0.23, relwidth=0.95)

        # Criar Widgets para area de inserir coordenadas para impressão no cartão
        self.frame_data_posicion = LabelFrame(
            self.frame_main,
            bg=self.gray1,
            text="Dados",
            relief=GROOVE,
            font=("Robot", 12),
        )
        self.frame_data_posicion.place(
            relx=0.02, rely=0.24, relwidth=0.25, relheight=0.75
        )

        # Widgets valores para nome
        self.label_name = Label(
            self.frame_data_posicion,
            text="Nome ",
            fg=self.black,
            bg=self.gray1,
            font=("Robot", 10),
            anchor="w",
        )
        self.label_name.place(relx=0.01, rely=0.005, relwidth=0.25, relheight=0.05)
        self.label_name_x = Label(
            self.frame_data_posicion,
            text="X: ",
            fg=self.black,
            bg=self.gray1,
            font=("Robot", 10),
            anchor="w",
        )
        self.label_name_x.place(relx=0.01, rely=0.07, relwidth=0.11, relheight=0.05)
        self.entry_name_x = Spinbox(
            self.frame_data_posicion,
            textvariable=self.namex_entry,
            from_=0,
            to=320,
            increment=5,
            bg=self.white,
            validate="key",
            validatecommand=(self.root.register(self.validate_entry), "%P"),
            font=("Robot", 10),
        )
        self.entry_name_x.place(relx=0.14, rely=0.07, relwidth=0.33, relheight=0.05)
        self.label_name_y = Label(
            self.frame_data_posicion,
            text="Y: ",
            fg=self.black,
            bg=self.gray1,
            font=("Robot", 10),
            anchor="w",
        )
        self.label_name_y.place(relx=0.51, rely=0.07, relwidth=0.11, relheight=0.05)
        self.entry_name_y = Spinbox(
            self.frame_data_posicion,
            textvariable=self.namey_entry,
            from_=0,
            to=320,
            increment=5,
            bg=self.white,
            validate="key",
            validatecommand=(self.root.register(self.validate_entry), "%P"),
            font=("Robot", 10),
        )
        self.entry_name_y.place(relx=0.63, rely=0.07, relwidth=0.33, relheight=0.05)
        self.label_fontsize_name = Label(
            self.frame_data_posicion,
            text="Tamanho: ",
            fg=self.black,
            bg=self.gray1,
            font=("Robot", 10),
            anchor="w",
        )
        self.label_fontsize_name.place(
            relx=0.01, rely=0.135, relwidth=0.40, relheight=0.05
        )
        self.entry_fontsize_name = Spinbox(
            self.frame_data_posicion,
            textvariable=self.name_size_entry,
            from_=2,
            to=320,
            increment=2,
            bg=self.white,
            validate="key",
            validatecommand=(self.root.register(self.validate_entry), "%P"),
            font=("Robot", 10),
        )
        self.entry_fontsize_name.place(
            relx=0.42, rely=0.135, relwidth=0.55, relheight=0.05
        )
        self.label_color_name = Label(
            self.frame_data_posicion,
            text="Cor: ",
            fg=self.black,
            bg=self.gray1,
            font=("Robot", 10),
            anchor="w",
        )
        self.label_color_name.place(relx=0.01, rely=0.20, relwidth=0.20, relheight=0.05)
        self.button_color_name = ctk.CTkButton(
            self.frame_data_posicion,
            text="Selecionar Cor",
            font=("Robot", 12),
            text_color=self.black,
            fg_color=self.blue1,
            command=self.choose_color_name,
            corner_radius=20,
        )
        self.button_color_name.place(
            relx=0.22, rely=0.20, relwidth=0.75, relheight=0.05
        )

        # Widgets valores para número do sócio
        self.label_number = Label(
            self.frame_data_posicion,
            text="Nº Sócio ",
            fg=self.black,
            bg=self.gray1,
            font=("Robot", 10),
            anchor="w",
        )
        self.label_number.place(relx=0.01, rely=0.30, relwidth=0.35, relheight=0.05)
        self.label_number_x = Label(
            self.frame_data_posicion,
            text="X: ",
            fg=self.black,
            bg=self.gray1,
            font=("Robot", 10),
            anchor="w",
        )
        self.label_number_x.place(relx=0.01, rely=0.37, relwidth=0.11, relheight=0.05)
        self.entry_number_x = Spinbox(
            self.frame_data_posicion,
            textvariable=self.numberx_entry,
            from_=0,
            to=400,
            increment=5,
            bg=self.white,
            validate="key",
            validatecommand=(self.root.register(self.validate_entry), "%P"),
            font=("Robot", 10),
        )
        self.entry_number_x.place(relx=0.14, rely=0.37, relwidth=0.33, relheight=0.05)
        self.label_number_y = Label(
            self.frame_data_posicion,
            text="Y: ",
            fg=self.black,
            bg=self.gray1,
            font=("Robot", 10),
            anchor="w",
        )
        self.label_number_y.place(relx=0.51, rely=0.37, relwidth=0.11, relheight=0.05)
        self.entry_number_y = Spinbox(
            self.frame_data_posicion,
            textvariable=self.numbery_entry,
            from_=2,
            to=400,
            increment=2,
            bg=self.white,
            validate="key",
            validatecommand=(self.root.register(self.validate_entry), "%P"),
            font=("Robot", 10),
        )
        self.entry_number_y.place(relx=0.63, rely=0.37, relwidth=0.33, relheight=0.05)
        self.label_fontsize_number = Label(
            self.frame_data_posicion,
            text="Tamanho: ",
            fg=self.black,
            bg=self.gray1,
            font=("Robot", 10),
            anchor="w",
        )
        self.label_fontsize_number.place(
            relx=0.01, rely=0.435, relwidth=0.40, relheight=0.05
        )
        self.entry_fontsize_number = Spinbox(
            self.frame_data_posicion,
            textvariable=self.number_size_entry,
            from_=0,
            to=400,
            increment=5,
            bg=self.white,
            validate="key",
            validatecommand=(self.root.register(self.validate_entry), "%P"),
            font=("Robot", 10),
        )
        self.entry_fontsize_number.place(
            relx=0.42, rely=0.435, relwidth=0.55, relheight=0.05
        )
        self.label_color_number = Label(
            self.frame_data_posicion,
            text="Cor: ",
            fg=self.black,
            bg=self.gray1,
            font=("Robot", 10),
            anchor="w",
        )
        self.label_color_number.place(
            relx=0.01, rely=0.505, relwidth=0.20, relheight=0.05
        )
        self.button_color_number = ctk.CTkButton(
            self.frame_data_posicion,
            font=("Robot", 12),
            text="Selecionar Cor",
            text_color=self.black,
            fg_color=self.blue1,
            command=self.choose_color_number,
            corner_radius=20,
        )
        self.button_color_number.place(
            relx=0.22, rely=0.505, relwidth=0.75, relheight=0.05
        )

        # Widgets valores para QR Code
        self.label_qrcode = Label(
            self.frame_data_posicion,
            text="QR Code ",
            fg=self.black,
            bg=self.gray1,
            font=("Robot", 10),
            anchor="w",
        )
        self.label_qrcode.place(relx=0.01, rely=0.605, relwidth=0.35, relheight=0.05)
        self.label_qrcode_x = Label(
            self.frame_data_posicion,
            text="X: ",
            fg=self.black,
            bg=self.gray1,
            font=("Robot", 10),
            anchor="w",
        )
        self.label_qrcode_x.place(relx=0.01, rely=0.675, relwidth=0.11, relheight=0.05)
        self.entry_qrcode_x = Spinbox(
            self.frame_data_posicion,
            textvariable=self.qrcodex_entry,
            from_=0,
            to=320,
            increment=5,
            bg=self.white,
            validate="key",
            validatecommand=(self.root.register(self.validate_entry), "%P"),
            font=("Robot", 10),
        )
        self.entry_qrcode_x.place(relx=0.14, rely=0.675, relwidth=0.33, relheight=0.05)
        self.label_qrcode_y = Label(
            self.frame_data_posicion,
            text="Y: ",
            fg=self.black,
            bg=self.gray1,
            font=("Robot", 10),
            anchor="w",
        )
        self.label_qrcode_y.place(relx=0.51, rely=0.675, relwidth=0.11, relheight=0.05)
        self.entry_qrcode_y = Spinbox(
            self.frame_data_posicion,
            textvariable=self.qrcodey_entry,
            from_=0,
            to=320,
            increment=5,
            bg=self.white,
            validate="key",
            validatecommand=(self.root.register(self.validate_entry), "%P"),
            font=("Robot", 10),
        )
        self.entry_qrcode_y.place(relx=0.63, rely=0.675, relwidth=0.33, relheight=0.05)
        self.label_fontsize_x_qrcode = Label(
            self.frame_data_posicion,
            text="Largura: ",
            fg=self.black,
            bg=self.gray1,
            font=("Robot", 10),
            anchor="w",
        )
        self.label_fontsize_x_qrcode.place(
            relx=0.01, rely=0.745, relwidth=0.50, relheight=0.05
        )
        self.entry_fontsize_x_qrcode = Spinbox(
            self.frame_data_posicion,
            textvariable=self.qrcode_entry_size_x,
            from_=0,
            to=320,
            increment=5,
            bg=self.white,
            validate="key",
            validatecommand=(self.root.register(self.validate_entry), "%P"),
            font=("Robot", 10),
        )
        self.entry_fontsize_x_qrcode.place(
            relx=0.47, rely=0.745, relwidth=0.50, relheight=0.05
        )
        self.label_fontsize_y_qrcode = Label(
            self.frame_data_posicion,
            text="Altura: ",
            fg=self.black,
            bg=self.gray1,
            font=("Robot", 10),
            anchor="w",
        )
        self.label_fontsize_y_qrcode.place(
            relx=0.01, rely=0.815, relwidth=0.50, relheight=0.05
        )
        self.entry_fontsize_y_qrcode = Spinbox(
            self.frame_data_posicion,
            textvariable=self.qrcode_entry_size_y,
            to=320,
            increment=5,
            bg=self.white,
            validate="key",
            validatecommand=(self.root.register(self.validate_entry), "%P"),
            font=("Robot", 10),
        )
        self.entry_fontsize_y_qrcode.place(
            relx=0.47, rely=0.815, relwidth=0.50, relheight=0.05
        )

        # Widget botão de visualizar dados na foto
        self.button_view = ctk.CTkButton(
            self.frame_data_posicion,
            command=self.data_config_card,
            text="Visualizar",
            text_color=self.black,
            fg_color=self.blue1,
            font=("Robot", 14, "bold"),
            corner_radius=20,
        )
        self.button_view.place(relx=0.18, rely=0.895, relwidth=0.62, relheight=0.08)

        # Criar frame visualização da imagem a ser impressa.
        self.frame_image_posicion = LabelFrame(
            self.frame_main,
            bg=self.gray1,
            text="Imagem",
            relief=GROOVE,
            font=("Robot", 12),
        )
        self.frame_image_posicion.place(
            relx=0.28, rely=0.24, relwidth=0.69, relheight=0.75
        )
        self.line_separator = ttk.Separator(
            self.frame_image_posicion, orient="horizontal", style="TSeparator"
        )
        style = ttk.Style()
        style.configure("TSeparator", background=self.black)
        self.line_separator.place(relx=0.02, rely=0.865, relwidth=0.95)

        # Widget para imprimir o cartão
        self.button_print = ctk.CTkButton(
            self.frame_image_posicion,
            text="Salvar",
            command=self.save_image_for_print,
            text_color=self.black,
            fg_color=self.blue1,
            font=("Robot", 14, "bold"),
            corner_radius=20,
        )
        self.button_print.place(relx=0.20, rely=0.895, relwidth=0.60, relheight=0.08)

        # Quando abrir as configurações, já aparece o caminho do qrcode
        self.link.set(self.query_data_xml()[0][1])
        self.entry_url.configure(state="normal")
        self.entry_url.delete(0, END)
        self.entry_url.insert(0, self.link.get())
        self.entry_url.configure(state="readonly")
        # setar valores iniciais para posicionar nome, numero e qrcode no cartão
        self.namex_entry.set(50)
        self.namey_entry.set(215)
        self.name_size_entry.set(14)
        self.button_color_name_set.set(self.black)
        self.numberx_entry.set(335)
        self.numbery_entry.set(135)
        self.number_size_entry.set(20)
        self.button_color_number_set.set(self.white)
        self.qrcodex_entry.set(287)
        self.qrcodey_entry.set(25)
        self.qrcode_entry_size_x.set(105)
        self.qrcode_entry_size_y.set(103)
        # chama função para mostrar a imagem a ser editada
        self.data_config_card()
        # atualização em tempo real da edição
        self.namex_entry.trace_add("write", lambda *args: self.data_config_card())
        self.namey_entry.trace_add("write", lambda *args: self.data_config_card())
        self.name_size_entry.trace_add("write", lambda *args: self.data_config_card())
        self.numberx_entry.trace_add("write", lambda *args: self.data_config_card())
        self.numbery_entry.trace_add("write", lambda *args: self.data_config_card())
        self.number_size_entry.trace_add("write", lambda *args: self.data_config_card())
        self.qrcodex_entry.trace_add("write", lambda *args: self.data_config_card())
        self.qrcodey_entry.trace_add("write", lambda *args: self.data_config_card())
        self.qrcode_entry_size_x.trace_add(
            "write", lambda *args: self.data_config_card()
        )
        self.qrcode_entry_size_y.trace_add(
            "write", lambda *args: self.data_config_card()
        )

    def entry_new_data_xml(self):

        self.frame_url_xml_2 = Frame(self.root, background=self.gray1)
        self.frame_url_xml_2.place(relx=0.02, rely=0.12, relwidth=0.95, relheight=0.10)
        self.label_url = Label(
            self.frame_url_xml_2,
            text="Insira novos dados: ",
            fg=self.black,
            bg=self.gray1,
            font=("Robot", 10),
            anchor="w",
        )
        self.label_url.place(relx=0.02, rely=0.10, relwidth=0.18, relheight=0.35)
        self.entry_url = Entry(
            self.frame_url_xml_2,
            justify=LEFT,
            bg=self.white,
        )
        self.entry_url.place(relx=0.263, rely=0.10, relwidth=0.683, relheight=0.325)
        self.button_url = ctk.CTkButton(
            self.frame_url_xml_2,
            text="Cancelar",
            command=self.frame_url_xml_2.destroy,
            text_color=self.black,
            fg_color=self.blue1,
            corner_radius=20,
            font=("Robot", 12, "bold"),
        )
        self.button_url.place(relx=0.02, rely=0.53, relwidth=0.17, relheight=0.40)

        self.button_url = ctk.CTkButton(
            self.frame_url_xml_2,
            text="Salvar",
            command=self.call_funcion_new_data_xml,
            text_color=self.black,
            fg_color=self.blue1,
            corner_radius=20,
            font=("Robot", 12, "bold"),
        )
        self.button_url.place(relx=0.21, rely=0.53, relwidth=0.17, relheight=0.40)

    def validate_entry(self, value):
        """
        Função que permite apenas números nos campos de coordenadas e tamanho da fonte

        """
        if value.isdigit():
            return True
        else:
            return False

    def open_image(self):

        self.open_photo = filedialog.askopenfilename()

        if self.open_photo:

            try:
                self.save_path = self.open_photo
                if self.save_path:

                    # inserir caminho da foto no widget
                    self.entry_download.configure(state="normal")
                    self.entry_download.delete(0, END)
                    self.entry_download.insert(0, self.save_path)
                    self.entry_download.configure(state="readonly")
                    # inserir valores iniciais as coordenadas

                # abrir imagem

                with Image.open(self.open_photo) as self.img:
                    self.img = self.img.resize((420, 265))
                    self.path_img = self.img

                self.img = ImageTk.PhotoImage(self.img)
                self.entry_download.delete(0, END)
                self.entry_download.insert(0, self.save_path)
                # Campo com coordenadas já iniciam com valores iniciais pre definidos para nome número e qrcode
                self.namex_entry.set(50)
                self.namey_entry.set(215)
                self.name_size_entry.set(15)
                self.button_color_name_set.set("black")
                self.button_color_number_set.set("white")
                self.button_color_name.configure(fg_color=self.blue1)
                self.button_color_number.configure(fg_color=self.blue1)
                self.numberx_entry.set(335)
                self.numbery_entry.set(135)
                self.number_size_entry.set(20)
                self.qrcodex_entry.set(287)
                self.qrcodey_entry.set(25)
                self.qrcode_entry_size_x.set(105)
                self.qrcode_entry_size_y.set(103)
                self.label_image = Label(self.frame_image_posicion, image=self.img)
                self.label_image.place(
                    relx=0.01, rely=0.01, relwidth=0.97, relheight=0.85
                )
            except Exception as e:

                print(f"Erro ao processar a imagem: {e}")
        else:
            # reseta a variavel em caso de cancela a escolha da imagem
            self.open_photo = StringVar()

    def data_config_card(self):
        """
        Função para configurar posicionamento, tamanho e cor do: nome, número do sócio e Qrcode do cliente
        """

        if self.open_photo:
            if not isinstance(self.open_photo, str):

                os.makedirs("image_card_base", exist_ok=True)
                os.makedirs("image_card", exist_ok=True)
                if not os.path.exists(
                    os.path.abspath("image_card_base/model_card.png")
                ):
                    shutil.copy(
                        self.resource_path("model_card.png"),
                        os.path.abspath(os.path.join("image_card_base")),
                    )
                self.path = Image.open(
                    os.path.abspath("image_card_base/model_card.png")
                )
                self.path = self.path.resize((420, 265))

                self.draw = ImageDraw.Draw(self.path)
                entries = [
                    int(self.name_size_entry.get()),
                    int(self.number_size_entry.get()),
                    int(self.qrcode_entry_size_x.get()),
                    int(self.qrcode_entry_size_y.get()),
                ]

                # Verificação simplificada

                if all(value > 0 for value in entries):

                    self.draw.text(
                        (self.namex_entry.get(), self.namey_entry.get()),
                        self.values[0][1],
                        fill=self.button_color_name_set.get(),
                        font=ImageFont.truetype(
                            "arial.ttf", self.name_size_entry.get()
                        ),
                        encoding="utf-8",
                    )
                    self.draw.text(
                        (self.numberx_entry.get(), self.numbery_entry.get()),
                        str(self.values[0][0]),
                        fill=self.button_color_number_set.get(),
                        font_size=self.number_size_entry.get(),
                    )
                    self.path_qrcode = Image.open(self.data_selected_clients[0][3])

                    self.path_qrcode = self.path_qrcode.resize(
                        (self.qrcode_entry_size_x.get(), self.qrcode_entry_size_y.get())
                    )
                    self.path.paste(
                        self.path_qrcode,
                        (self.qrcodex_entry.get(), self.qrcodey_entry.get()),
                    )
                else:
                    messagebox.showwarning(
                        "Atenção", "O tamanho da fonte não pode ser menor que 1"
                    )
                # caminho da imagem para salvar cartão
                self.image_card_for_save = self.path

                self.path = ImageTk.PhotoImage(self.path)

                self.label_image = Label(self.frame_image_posicion, image=self.path)
                self.label_image.place(
                    relx=0.01, rely=0.01, relwidth=0.97, relheight=0.85
                )

            else:

                self.path = Image.open(self.save_path)
                self.path = self.path.resize((420, 265))

                self.draw = ImageDraw.Draw(self.path)
                entries = [
                    int(self.name_size_entry.get()),
                    int(self.number_size_entry.get()),
                    int(self.qrcode_entry_size_x.get()),
                    int(self.qrcode_entry_size_y.get()),
                ]

                # Verificação simplificada

                if all(value > 0 for value in entries):

                    self.draw.text(
                        (self.namex_entry.get(), self.namey_entry.get()),
                        self.values[0][1],
                        fill=self.button_color_name_set.get(),
                        # font_size=self.name_size_entry.get(),
                        font=ImageFont.truetype(
                            "arial.ttf", self.name_size_entry.get()
                        ),
                        encoding="utf-8",
                    )
                    self.draw.text(
                        (self.numberx_entry.get(), self.numbery_entry.get()),
                        str(self.values[0][0]),
                        fill=self.button_color_number_set.get(),
                        font_size=self.number_size_entry.get(),
                    )
                    self.path_qrcode = Image.open(self.data_selected_clients[0][3])

                    self.path_qrcode = self.path_qrcode.resize(
                        (self.qrcode_entry_size_x.get(), self.qrcode_entry_size_y.get())
                    )
                    self.path.paste(
                        self.path_qrcode,
                        (self.qrcodex_entry.get(), self.qrcodey_entry.get()),
                    )
                else:
                    messagebox.showwarning(
                        "Atenção", "O tamanho da fonte não pode ser menor que 1"
                    )
                # caminho da imagem para salvar cartão
                self.image_card_for_save = self.path

                self.path = ImageTk.PhotoImage(self.path)

                self.label_image = Label(self.frame_image_posicion, image=self.path)
                self.label_image.place(
                    relx=0.01, rely=0.01, relwidth=0.97, relheight=0.85
                )

        else:
            messagebox.showwarning("Atenção", "Selecione um foto")

    def save_image_for_print(self):

        message = messagebox.askokcancel(
            "Salvar Imagem", "Tem certeza que quer salvar está imagem?"
        )
        if message:
            if os.path.exists(str(self.open_photo)):
                for clients in self.list_dict:

                    os.makedirs("image_card_base", exist_ok=True)
                    os.makedirs("image_card", exist_ok=True)

                    shutil.copy(
                        self.open_photo,
                        os.path.abspath(
                            os.path.join("image_card_base", "model_card.png")
                        ),
                    )

                    self.image_base = os.path.abspath(
                        os.path.join("image_card_base", "model_card.png")
                    )

                    with Image.open(self.open_photo) as self.img:
                        self.img = self.img.resize((420, 265))
                        self.path_img = self.img
                    self.draw = ImageDraw.Draw(self.img)
                    entries = [
                        int(self.name_size_entry.get()),
                        int(self.number_size_entry.get()),
                        int(self.qrcode_entry_size_x.get()),
                        int(self.qrcode_entry_size_y.get()),
                    ]

                    # Verificação simplificada

                    if all(value > 0 for value in entries):
                        self.draw.text(
                            (self.namex_entry.get(), self.namey_entry.get()),
                            clients[3],
                            fill=self.config_color_combobox_name(),
                            font=ImageFont.truetype(
                                "arial.ttf", self.name_size_entry.get()
                            ),
                            encoding="utf-8",
                        )
                        self.draw.text(
                            (self.numberx_entry.get(), self.numbery_entry.get()),
                            clients[0],
                            fill=self.config_color_combobox_number(),
                            font_size=self.number_size_entry.get(),
                        )
                        for query_number in self.query_data_card():

                            if str(query_number[1]) == clients[0]:
                                self.path_qrcode = Image.open(query_number[3])

                                self.path_qrcode = self.path_qrcode.resize(
                                    (
                                        self.qrcode_entry_size_x.get(),
                                        self.qrcode_entry_size_y.get(),
                                    )
                                )
                                self.path_img.paste(
                                    self.path_qrcode,
                                    (
                                        self.qrcodex_entry.get(),
                                        self.qrcodey_entry.get(),
                                    ),
                                )
                                path_card = os.path.abspath(
                                    os.path.join(
                                        "image_card",
                                        rf"{clients[0]}_{clients[3].replace(' ', '')}_card.png",
                                    )
                                )
                                self.list_cards_for_printer.append(path_card)

                                self.path_img.save(path_card)
                                # salvar caminho no banco de dados
                                self.open_sql()
                                card = f"Update Socios SET card =  ? WHERE number = ?"
                                self.cursor.execute(card, (path_card, clients[0]))
                                self.close_sql()

            else:

                for clients in self.list_dict:

                    os.makedirs("image_card_base", exist_ok=True)
                    os.makedirs("image_card", exist_ok=True)
                    # if not os.path.exists(os.path.abspath("image_card_base/model_card.png")):
                    #     shutil.copy(
                    #         self.resource_path("model_card.png"),
                    #         os.path.abspath(os.path.join("image_card_base")),
                    #     )
                    self.image_base = os.path.abspath(
                        os.path.join("image_card_base", "model_card.png")
                    )

                    with Image.open(self.image_base) as self.img:
                        self.img = self.img.resize((420, 265))
                        self.path_img = self.img
                    self.draw = ImageDraw.Draw(self.img)
                    entries = [
                        int(self.name_size_entry.get()),
                        int(self.number_size_entry.get()),
                        int(self.qrcode_entry_size_x.get()),
                        int(self.qrcode_entry_size_y.get()),
                    ]

                    # Verificação simplificada

                    if all(value > 0 for value in entries):
                        self.draw.text(
                            (self.namex_entry.get(), self.namey_entry.get()),
                            clients[3],
                            fill=self.config_color_combobox_name(),
                            font=ImageFont.truetype(
                                "arial.ttf", self.name_size_entry.get()
                            ),
                            encoding="utf-8",
                        )
                        self.draw.text(
                            (self.numberx_entry.get(), self.numbery_entry.get()),
                            clients[0],
                            fill=self.config_color_combobox_number(),
                            font_size=self.number_size_entry.get(),
                        )
                        for query_number in self.query_data_card():

                            if str(query_number[1]) == clients[0]:
                                self.path_qrcode = Image.open(query_number[3])

                                self.path_qrcode = self.path_qrcode.resize(
                                    (
                                        self.qrcode_entry_size_x.get(),
                                        self.qrcode_entry_size_y.get(),
                                    )
                                )
                                self.path_img.paste(
                                    self.path_qrcode,
                                    (
                                        self.qrcodex_entry.get(),
                                        self.qrcodey_entry.get(),
                                    ),
                                )
                                path_card = os.path.abspath(
                                    os.path.join(
                                        "image_card",
                                        rf"{clients[0]}_{clients[3].replace(' ', '')}_card.png",
                                    )
                                )
                                self.list_cards_for_printer.append(path_card)

                                self.path_img.save(path_card)
                                # salvar caminho no banco de dados
                                self.open_sql()
                                card = f"Update Socios SET card =  ? WHERE number = ?"
                                self.cursor.execute(card, (path_card, clients[0]))
                                self.close_sql()

        else:
            return
        self.click_function_main_treeview()

    def choice_printer(self):
        """
        :return: lista de todas as impressoras
        """
        try:
            printers = [printer[2] for printer in win32print.EnumPrinters(2)]
            return printers
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível listar as impressoras: {e}")
            return []

    def group_pdf_image(self, list_image, path_exit):
        """
        Gera um único PDF com as imagens no tamanho padrão de cartão multibanco (85,6 mm x 53,98 mm).
        """

        pdf = FPDF(unit="mm", format=(85.6, 53.98))  # Tamanho do cartão
        for index, image in enumerate(list_image):

            try:
                img = Image.open(image)

                # Redimensionar a imagem para caber no cartão
                img = img.resize((1011, 637))

                # Salvar uma versão temporária redimensionada
                temp_imagem = os.path.abspath(rf"image_card/temp{index}.jpg")
                img.save(temp_imagem)

                # Adicionar a imagem ao PDF
                pdf.add_page()
                pdf.image(temp_imagem, x=0, y=0, w=85.6, h=53.98)

                # Remover a imagem temporária
                os.remove(temp_imagem)
            except Exception as e:
                print(f"Erro ao processar a imagem {image}: {e}")
                continue
        pdf.output(path_exit)

    def open_printer(self, event):
        """
        Seleciona a impressora e executa comando windows para iniciar a impressão
        :return:
        """
        print(self.combobox_type_select.get(), "open_printer")
        select_printer = self.combobox_type_select.get()
        # win32print.SetDefaultPrinter(select_printer)

        if self.check_print_labels == "":
            # Criar um PDF com todas as imagens no tamanho correto
            path_pdf = os.path.abspath(r"image_card/cartoes_para_impressao.pdf")
            self.group_pdf_image(self.list_cards_for_printer, path_pdf)

            try:
                win32api.ShellExecute(0, "print", path_pdf, None, ".", 0)
                print(f"Impressora selecionada: {select_printer}")
            except:

                print("continue print")
            finally:
                self.click_function_main_treeview()
                self.window_printer.destroy()
        elif self.check_print_labels == "label":
            try:
                win32api.ShellExecute(0, "print", self.pdf_label_path, None, ".", 0)
                print(f"Impressora selecionada: {select_printer}")
            except:

                print("continue print")
            finally:
                self.click_function_main_treeview()
                self.window_printer.destroy()
        else:
            try:
                win32api.ShellExecute(0, "print", self.pdf_letter_path, None, ".", 0)
                print(f"Impressora selecionada: {select_printer}")
            except:

                print("continue print")
            finally:
                self.click_function_main_treeview()
                self.window_printer.destroy()

    def on_close_printer(self):
        """
        return: função para quando o usuario clicar em fechar janela do app(impressora)
        """
        self.click_function_main_treeview()
        self.window_printer.grab_release()
        self.window_printer.destroy()

    def on_close_entry_xml(self):
        """
        return: função para quando o usuario clicar em fechar janela do app(impressora)
        """
        self.click_function_main_treeview()
        self.window_xml.grab_release()
        self.window_xml.destroy()

    def on_close_layout_print_label(self):
        """
        return: função para quando o usuario clicar em fechar janela do app(etiqueta)
        """
        self.click_function_main_treeview()
        self.window_ticket.grab_release()
        self.window_ticket.destroy()

    def screen_printer(self):

        try:
            self.window_printer = ctk.CTkToplevel()
            self.window_printer.title("Sócio Online")
            self.window_printer.after(
                200,
                lambda: self.window_printer.iconbitmap(self.resource_path("logo.ico")),
            )
            # Centralizar o app ao iniciar
            width_screen = self.window_printer.winfo_screenwidth()
            height_screen = self.window_printer.winfo_screenheight()
            pos_x = (width_screen / 2) - (800 / 2)
            pos_y = (height_screen / 2) - (500 / 2)
            self.window_printer.geometry(
                "%dx%d+%d+%d" % (width_screen, height_screen, pos_x, pos_y)
            )
            # altera titulo da janela
            self.window_printer.geometry("400x300")
            self.window_printer.configure(fg_color=self.gray1)
            self.window_printer.resizable(False, False)
            self.window_printer.protocol("WM_DELETE_WINDOW", self.on_close_printer)
            self.button_select_printer = ctk.CTkButton(
                self.window_printer,
                text="Voltar",
                text_color=self.black,
                corner_radius=20,
                fg_color=self.blue1,
                font=("Robot", 12, "bold"),
                command=self.click_function_main_treeview,
                hover=True,
            )

            self.button_select_printer.place(
                relx=0.02, rely=0.02, relwidth=0.17, relheight=0.08
            )
            self.line_separator = ttk.Separator(
                self.window_printer, orient="horizontal", style="TSeparator"
            )
            style = ttk.Style()
            style.configure("TSeparator", background=self.black)
            self.line_separator.place(relx=0.02, rely=0.13, relwidth=0.95)
            self.label_select_printer = Label(
                self.window_printer,
                text="Selecione impressora: ",
                font=("Robot", 14),
                bg=self.gray1,
            )
            self.label_select_printer.place(relx=0.03, rely=0.20)

            self.combobox_type = ctk.CTkComboBox(
                self.window_printer,
                values=self.choice_printer(),
                font=("Robot", 12, "bold"),
                corner_radius=10,
                fg_color=self.gray1,
                dropdown_fg_color=self.gray2,
                dropdown_hover_color=self.blue1,
                dropdown_text_color=self.black,
                text_color=self.black,
                state="readonly",
                variable=self.combobox_type_select,
                command=self.open_printer,
            )
            self.combobox_type.place(relx=0.03, rely=0.35, relwidth=0.7, relheight=0.10)
            self.combobox_type_select.set(win32print.GetDefaultPrinter())
            # Vincula o evento de seleção ao comando
            # self.combobox_type.bind("<<ComboboxSelected>>", self.open_printer)
            self.window_printer.grab_set()
            print(self.combobox_type_select.get())
        except:
            messagebox.showwarning(
                "Atenção", "Selecione um foto e clique em visualizar"
            )

    def data_xml_main_frame(self):
        """
        Janela para alterar dados xml
        """
        try:
            self.window_xml = ctk.CTkToplevel()
            self.window_xml.title("Sócio Online")

            # Centralizar o app ao iniciar
            width_screen = self.window_xml.winfo_screenwidth()
            height_screen = self.window_xml.winfo_screenheight()
            pos_x = (width_screen / 2) - (800 / 2)
            pos_y = (height_screen / 2) - (500 / 2)
            self.window_xml.geometry(
                "%dx%d+%d+%d" % (width_screen, height_screen, pos_x, pos_y)
            )
            # altera titulo da janela
            self.window_xml.geometry("400x120")
            self.window_xml.configure(fg_color=self.gray1)
            self.window_xml.resizable(False, False)
            ctk.set_appearance_mode("dark")
            self.window_xml.after(
                200, lambda: self.window_xml.iconbitmap(self.resource_path("logo.ico"))
            )
            self.window_xml.protocol("WM_DELETE_WINDOW", self.on_close_entry_xml)
            self.button_select_printer = ctk.CTkButton(
                self.window_xml,
                text="Voltar",
                fg_color=self.blue1,
                text_color=self.black,
                corner_radius=30,
                command=self.click_function_main_treeview,
                font=("Robot", 12, "bold"),
            )
            self.button_select_printer.place(
                relx=0.02, rely=0.025, relwidth=0.17, relheight=0.17
            )
            self.line_separator = ttk.Separator(
                self.window_xml, orient="horizontal", style="TSeparator"
            )
            style = ttk.Style()
            style.configure("TSeparator", background=self.black)
            self.line_separator.place(relx=0.02, rely=0.25, relwidth=0.95)
            self.label_url = Label(
                self.window_xml,
                text="Insira novos dados: ",
                fg=self.black,
                bg=self.gray1,
                font=("Robot", 10),
                anchor="w",
            )
            self.label_url.place(relx=0.35, rely=0.30, relwidth=0.50, relheight=0.1)
            self.entry_url = Entry(
                self.window_xml,
                justify=LEFT,
                bg=self.white,
            )
            self.entry_url.focus()
            self.entry_url.place(relx=0.05, rely=0.45, relwidth=0.9, relheight=0.15)
            self.button_url = ctk.CTkButton(
                self.window_xml,
                text="Cancelar",
                command=self.click_function_main_treeview,
                fg_color=self.blue1,
                text_color=self.black,
                corner_radius=30,
                font=("Robot", 12, "bold"),
            )
            self.button_url.place(relx=0.28, rely=0.7, relwidth=0.2, relheight=0.17)

            self.button_url = ctk.CTkButton(
                self.window_xml,
                text="Salvar",
                command=self.call_funcion_new_data_xml,
                fg_color=self.blue1,
                text_color=self.black,
                corner_radius=30,
                font=("Robot", 12, "bold"),
            )
            self.button_url.place(relx=0.53, rely=0.7, relwidth=0.17, relheight=0.17)
            # Quando abrir as configurações, já aparece o caminho do qrcode
            self.link.set(self.query_data_xml()[0][1])
            self.entry_url.configure(state="normal")
            self.entry_url.delete(0, END)
            self.entry_url.insert(0, self.link.get())
            self.window_xml.grab_set()
        except:
            messagebox.showwarning("Atenção", "Erro ao executar")

    def call_funcion_new_data_xml(self):
        """
        função do import_data_xml para alterar os dados xml dos sócios no banco de dados
        :return:
        """
        self.new_data_xml()

    def layout_print_label(self):

        try:
            self.window_ticket = ctk.CTkToplevel()
            self.window_ticket.title("Sócio Online")

            # Centralizar o app ao iniciar
            width_screen = self.window_ticket.winfo_screenwidth()
            height_screen = self.window_ticket.winfo_screenheight()
            pos_x = (width_screen / 2) - (800 / 2)
            pos_y = (height_screen / 2) - (500 / 2)
            self.window_ticket.geometry(
                "%dx%d+%d+%d" % (width_screen, height_screen, pos_x, pos_y)
            )
            # altera titulo da janela
            self.window_ticket.geometry("400x300")
            self.window_ticket.configure(fg_color=self.gray1)
            self.window_ticket.resizable(False, False)
            self.window_ticket.after(
                200,
                lambda: self.window_ticket.iconbitmap(self.resource_path("logo.ico")),
            )
            self.window_ticket.protocol(
                "WM_DELETE_WINDOW", self.on_close_layout_print_label
            )

            self.button_select_printer = ctk.CTkButton(
                self.window_ticket,
                text="Voltar",
                fg_color=self.blue1,
                text_color=self.black,
                corner_radius=30,
                command=self.click_function_main_treeview,
                font=("Robot", 12, "bold"),
            )
            self.button_select_printer.place(
                relx=0.02, rely=0.020, relwidth=0.2, relheight=0.07
            )
            self.line_separator = ttk.Separator(
                self.window_ticket, orient="horizontal", style="TSeparator"
            )
            style = ttk.Style()
            style.configure("TSeparator", background=self.black)
            self.line_separator.place(relx=0.02, rely=0.10, relwidth=0.95)
            self.laber_sender = Label(
                self.window_ticket,
                text="Edição Etiquetas ",
                fg=self.black,
                bg=self.gray1,
                font=("Robot", 14),
                anchor="center",
                relief="sunken",
                borderwidth=2,
            )
            self.laber_sender.place(relx=0.02, rely=0.12, relwidth=0.95, relheight=0.15)

            self.label_frame_config = LabelFrame(
                self.window_ticket,
                text="Página",
                bg=self.gray1,
                font=("arial", 11),
                border=3,
            )
            self.label_frame_config.place(
                relx=0.02, rely=0.29, relwidth=0.45, relheight=0.4
            )

            self.label_frame_config2 = LabelFrame(
                self.window_ticket,
                text="Texto",
                bg=self.gray1,
                font=("arial", 10),
                border=3,
            )
            self.label_frame_config2.place(
                relx=0.50, rely=0.29, relwidth=0.47, relheight=0.4
            )

            self.label_width = Label(
                self.label_frame_config,
                text="Largura: ",
                fg=self.black,
                bg=self.gray1,
                font=("Robot", 10),
                anchor="w",
            )
            self.label_width.place(relx=0.01, rely=0.1, relwidth=0.3, relheight=0.2)
            self.entry_width = Spinbox(
                self.label_frame_config,
                bg=self.white,
                from_=30,
                to=5000,
                increment=10,
                validate="key",
                textvariable=self.width_label_entry,
                validatecommand=(self.root.register(self.validate_entry), "%P"),
                font=("Robot", 10),
            )

            self.entry_width.place(relx=0.35, rely=0.1, relwidth=0.25, relheight=0.2)

            self.label_mm_width = Label(
                self.label_frame_config,
                text="mm ",
                fg=self.black,
                bg=self.gray1,
                font=("Robot", 10),
                anchor="w",
            )
            self.label_mm_width.place(relx=0.6, rely=0.1, relwidth=0.15, relheight=0.2)

            self.label_height = Label(
                self.label_frame_config,
                text="Altura: ",
                fg=self.black,
                bg=self.gray1,
                font=("Robot", 10),
                anchor="w",
            )
            self.label_height.place(relx=0.01, rely=0.5, relwidth=0.3, relheight=0.2)
            self.entry_height = Spinbox(
                self.label_frame_config,
                bg=self.white,
                from_=30,
                to=3000,
                increment=5,
                validate="key",
                textvariable=self.height_label_entry,
                validatecommand=(self.root.register(self.validate_entry), "%P"),
                font=("Robot", 10),
            )

            self.entry_height.place(relx=0.35, rely=0.5, relwidth=0.25, relheight=0.2)

            self.label_mm_height = Label(
                self.label_frame_config,
                text="mm ",
                fg=self.black,
                bg=self.gray1,
                font=("Robot", 10),
                anchor="w",
            )
            self.label_mm_height.place(relx=0.6, rely=0.5, relwidth=0.15, relheight=0.2)

            self.label_font = Label(
                self.label_frame_config2,
                text="Tamanho: ",
                fg=self.black,
                bg=self.gray1,
                font=("Robot", 10),
                anchor="w",
            )
            self.label_font.place(relx=0.01, rely=0.1, relwidth=0.33, relheight=0.2)
            self.entry_font = Spinbox(
                self.label_frame_config2,
                bg=self.white,
                textvariable=self.size_text_label,
                from_=5,
                to=50,
                increment=1,
                validate="key",
                validatecommand=(self.root.register(self.validate_entry), "%P"),
                font=("Robot", 10),
            )

            self.entry_font.place(relx=0.41, rely=0.1, relwidth=0.25, relheight=0.2)

            self.label_mm_font = Label(
                self.label_frame_config2,
                text="mm ",
                fg=self.black,
                bg=self.gray1,
                font=("Robot", 10),
                anchor="w",
            )
            self.label_mm_font.place(relx=0.66, rely=0.1, relwidth=0.15, relheight=0.2)

            self.label_foreground = Label(
                self.label_frame_config2,
                text="Cor: ",
                fg=self.black,
                bg=self.gray1,
                font=("Robot", 10),
                anchor="w",
            )
            self.label_foreground.place(
                relx=0.01, rely=0.4, relwidth=0.3, relheight=0.2
            )
            self.entry_foreground = ctk.CTkButton(
                self.label_frame_config2,
                fg_color=self.gray2,
                text_color=self.black,
                corner_radius=20,
                text="Selecionar Cor",
                command=self.choose_color_label,
                font=("Robot", 12),
            )

            self.entry_foreground.place(
                relx=0.3, rely=0.4, relwidth=0.62, relheight=0.22
            )

            self.label_background = Label(
                self.label_frame_config2,
                text="Fundo: ",
                fg=self.black,
                bg=self.gray1,
                font=("Robot", 10),
                anchor="w",
            )
            self.label_background.place(
                relx=0.01, rely=0.7, relwidth=0.26, relheight=0.2
            )
            self.entry_background = ctk.CTkButton(
                self.label_frame_config2,
                fg_color=self.gray2,
                text_color=self.black,
                corner_radius=20,
                text="Selecionar Cor",
                command=self.choose_color_background_label,
                font=("Robot", 12),
            )

            self.entry_background.place(
                relx=0.3, rely=0.7, relwidth=0.62, relheight=0.22
            )

            self.label_view = Label(
                self.window_ticket,
                textvariable=self.text_preview,
                fg=self.black,
                bg=self.white,
                font=("Robot", 10),
                anchor="center",
            )
            self.label_view.place(relx=0.02, rely=0.7, relwidth=0.95, relheight=0.18)

            self.button_url = ctk.CTkButton(
                self.window_ticket,
                text="Cancelar",
                fg_color=self.blue1,
                text_color=self.black,
                corner_radius=20,
                command=self.click_function_main_treeview,
                font=("Robot", 12, "bold"),
            )
            self.button_url.place(relx=0.26, rely=0.9, relwidth=0.21, relheight=0.08)

            self.button_url = ctk.CTkButton(
                self.window_ticket,
                text="Salvar",
                fg_color=self.blue1,
                text_color=self.black,
                corner_radius=20,
                command=self.print_pdf_label,
                font=("Robot", 12, "bold"),
            )
            self.button_url.place(relx=0.51, rely=0.9, relwidth=0.21, relheight=0.08)

            # Setendo valores iniciais para impressao das etiquetas
            self.color_label_letter_rgb = (0, 0, 0)
            self.background_label_letter_rgb = (255, 255, 255)
            self.width_label_entry.set(210)
            self.height_label_entry.set(50)
            self.color_label_letter.set(f"#000000")
            self.background_label_letter.set(f"#ffffff")
            self.widht_label.set(150)
            self.height_label.set(50)
            self.text_preview.set("Exemplo de Texto")
            self.size_text_label.set(12)
            self.size_text_label.trace_add(
                "write", lambda *args: self.preview_label_print()
            )
            self.color_label_letter.trace_add(
                "write", lambda *args: self.preview_label_print()
            )
            self.background_label_letter.trace_add(
                "write", lambda *args: self.preview_label_print()
            )
            self.window_ticket.grab_set()
        except:
            messagebox.showwarning("Atenção", "erro")

    def preview_label_print(self):
        size = self.size_text_label.get()
        color = self.color_label_letter.get()
        background = self.background_label_letter.get()
        self.label_view.config(font=("Arial", size), fg=color, bg=background)


if __name__ == "__main__":
    App_Card()
