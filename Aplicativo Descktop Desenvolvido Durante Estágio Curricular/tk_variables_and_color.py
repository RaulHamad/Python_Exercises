from tkinter import *
from tkinter import colorchooser


class Variables_and_colors:

    def variable(self):

        # variavel para campo de pesquisa de clientes
        self.entry_search = StringVar()
        # lista com os caminhos salvos para imprimir
        self.list_cards_for_printer = list()
        # variavel na função open_image para exibir texto no entry do carregamento
        self.save_path = StringVar()
        self.open_photo = StringVar()
        self.values_edit_card = []

        # variaveis de posicionamento, font e cor dos nomes,nº sócio e qrcode
        self.namex_entry = IntVar()
        self.namey_entry = IntVar()
        self.name_size_entry = IntVar()
        self.name_color = StringVar()

        self.numberx_entry = IntVar()
        self.numbery_entry = IntVar()
        self.number_size_entry = IntVar()
        self.number_color = StringVar()

        self.qrcodex_entry = IntVar()
        self.qrcodey_entry = IntVar()
        self.qrcode_entry_size_x = IntVar()
        self.qrcode_entry_size_y = IntVar()

        # Variavel para armazenar dados do cliente selecionado e exibir na configuração do cartão
        self.data_client = list()

        # Variável que armazena nome e número do cliente selecionado na treeview
        self.values = []
        ##variável do link de dados xml
        self.link = StringVar()
        # variavel para armazenar os menus do self.file_menu
        self.menu_name = []
        # variavel com todos os dados da treeview
        self.filtered_names = []
        # variavel para impressao de etiquetas Função Self.layout_print_label
        self.color_label_letter = StringVar()
        self.background_label_letter = StringVar()
        self.widht_label = IntVar()
        self.height_label = IntVar()
        self.size_text_label = IntVar()
        self.text_preview = StringVar()
        self.width_label_entry = IntVar()
        self.height_label_entry = IntVar()
        self.color_label_letter_rgb = (0,0,0)
        self.background_label_letter_rgb = (255,255,255)
        #variaveis para armazenar as cores da função data_config_Card
        self.button_color_name_set = StringVar()
        self.button_color_number_set = StringVar()
        #variavel do combobox para abrir a impressaora na função screen_printer
        self.combobox_type_select = StringVar()

    def colors(self):
        self.blue1 = "#1E90FF"
        self.gray1 = "lavender"
        self.black = "black"
        self.gray2 = "#A9A9A9"
        self.white = "white"
        self.list_colors = [
            "Preto",
            "Branco",
            "Vermelho",
            "Azul",
            "Verde",
            "Cinza",
            "Rosa",
            "Marrom",
        ]

    def config_color_combobox_name(self, event=None):
        color_combobox_name = self.button_color_name_set.get()

        if color_combobox_name == "Preto":
            color_combobox_name = "black"
        elif color_combobox_name == "Branco":
            color_combobox_name = "white"
        elif color_combobox_name == "Vermelho":
            color_combobox_name = "red"
        elif color_combobox_name == "Azul":
            color_combobox_name = "blue"
        elif color_combobox_name == "Verde":
            color_combobox_name = "green"
        elif color_combobox_name == "Cinza":
            color_combobox_name = "gray"
        elif color_combobox_name == "Rosa":
            color_combobox_name = "pink"
        elif color_combobox_name == "Marrom":
            color_combobox_name = "brown"
        return color_combobox_name

    def config_color_combobox_number(self, event=None):
        color_combobox_number = self.button_color_number_set.get()

        if color_combobox_number == "Branco":
            color_combobox_number = "White"
        elif color_combobox_number == "Preto":
            color_combobox_number = "black"
        elif color_combobox_number == "Vermelho":
            color_combobox_number = "red"
        elif color_combobox_number == "Azul":
            color_combobox_number = "blue"
        elif color_combobox_number == "Verde":
            color_combobox_number = "green"
        elif color_combobox_number == "Cinza":
            color_combobox_number = "gray"
        elif color_combobox_number == "Rosa":
            color_combobox_number = "pink"
        elif color_combobox_number == "Marrom":
            color_combobox_number = "brown"
        return color_combobox_number

    def choose_color_number(self):
        self.color = colorchooser.askcolor(title="Escolha uma cor")[1]
        if self.color:

            self.button_color_number_set.set(self.color)
            self.button_color_number.configure(fg_color=self.button_color_number_set.get())
            self.data_config_card()

    def choose_color_name(self):
        self.color = colorchooser.askcolor(title="Escolha uma cor")[1]
        if self.color:

            self.button_color_name_set.set(self.color)
            self.button_color_name.configure(fg_color=self.button_color_name_set.get())
            self.data_config_card()

    def choose_color_label(self):
        self.color2 = colorchooser.askcolor(title="Escolha uma cor")
        if self.color2:
            self.color_label_letter_rgb = self.color2[0][0],self.color2[0][1],self.color2[0][2]

            self.color_label_letter.set(self.color2[1])
            self.entry_foreground.configure(fg_color=self.color_label_letter.get())
            self.window_ticket.lift()

    def choose_color_background_label(self):
        #self.color2 é uma tupla com valor hexadecimal e RGB
        self.color2 = colorchooser.askcolor(title="Escolha uma cor")
        if self.color2:
            self.background_label_letter_rgb = self.color2[0][0],self.color2[0][1],self.color2[0][2]
            self.background_label_letter.set(self.color2[1])
            self.entry_background.configure(fg_color=self.background_label_letter.get())
            self.window_ticket.lift()
