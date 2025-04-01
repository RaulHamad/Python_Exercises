import requests
import xmltodict
import urllib3
import sqlite3
import os
from tkinter import messagebox
from urllib.parse import urlparse
import xml.etree.ElementTree as ET
import sys




class Data:

    def open_sql(self):
        """
        Abrir banco de dados e cria cursor
        """
        if not os.path.exists("database"):
            os.makedirs(os.path.abspath("database"))
        self.conn = sqlite3.connect("database/socioonline.db")
        self.cursor = self.conn.cursor()

    def close_sql(self):
        """
        Fecha banco de dados
        """
        self.conn.commit()
        self.conn.close()

    def table_data_xml(self):
        """
        Criação da tabela para armazenar link de dados xml dos sócios
        """

        data_table = """
                               CREATE TABLE IF NOT EXISTS Data (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               link      varchar(50) NOT NULL);
                               """
        self.cursor.execute(data_table)

    def table_data_card(self):
        """
        Criação da tabela para armazenar a imagem dos cartões dos sócios
        """

        card_table = """
                               CREATE TABLE IF NOT EXISTS Socios (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               number integer(10),
                               name varchar(50),
                               qrcode varchar(50),
                               card varchar(50) ,
                               email varchar(50),
                               phone varchar(50),
                               address varchar(100),
                               postal_code varchar(50),
                               country varchar(50));
                        
                               """
        self.cursor.execute(card_table)

    def query_data_card(self):

        self.open_sql()
        verify_table_data_card = "SELECT * FROM Socios "
        result = self.cursor.execute(verify_table_data_card)
        self.query_clients = result.fetchall()

        return self.query_clients

    def query_data_xml(self):

        self.open_sql()
        verify_table_data_xml = """SELECT * FROM Data"""
        result = self.cursor.execute(verify_table_data_xml)
        self.query_link = result.fetchall()

        return self.query_link

    def add_first_link_data_xml(self):
        self.open_sql()
        self.query_data_xml()
        if len(self.query_link) == 0:
            self.insert_data_xml(
                "https://rfstlobao.socios.online/xml-cards/data-files/demo.xml"
            )
            print('link adicionado')

        else:
            print("tabela ja possui dados")
        self.close_sql()



    def insert_data_xml(self, link):

        insert_data_xml = "INSERT INTO Data (link) VALUES (?)"
        self.cursor.execute(insert_data_xml, (link,))

    def init_data_base(self):
        """
        return: cria o banco de dados e as tabelas ao abrir o app
        """
        self.open_sql()
        self.table_data_xml()
        self.table_data_card()
        self.close_sql()

    def download_xml(self):
        """
        Faz o download de um arquivo XML a partir de uma URL obtida por query_data_xml
        e o salva no disco local como "demo.xml".
        """
        self.add_first_link_data_xml()

        urllib3.disable_warnings()
        # cabeçalhos como User-Agent para permitir o download
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        }

        url = f'{self.query_data_xml()[0][1]}'
        try:
            r = requests.get(url, allow_redirects=True, headers=headers, verify=False)
            #verificar e remover arquivo existente para substitui-lo
            if os.path.exists("socios.xml"):

                os.remove("socios.xml")
                print("Arquivo socios.xml existente foi excluído.")
            if r.status_code == 200:
                with open("socios.xml", "wb") as file:
                    file.write(r.content)
                print("Arquivo baixado com sucesso.")
            else:
                print(f"Erro ao acessar a URL: {r.status_code} - {r.reason}")

        except Exception as e:
            print(f"Erro geral: {e}")

    def is_valid_xml_data(self,url):
        """
        Verifica se o link fornecido é válido e retorna dados XML bem formados.

        """
        # Validar se a URL possui esquema (http/https) e domínio
        parsed_url = urlparse(url)
        if not (parsed_url.scheme and parsed_url.netloc):
            # messagebox.showinfo("URL inválida!", "Certifique-se de incluir o esquema (http ou https).")
            return False

        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            }
            # Fazer a requisição HTTP para o link
            response = requests.get(url, timeout=10,headers=headers)

            # Verificar se o status HTTP é 200 (requisição bem-sucedida)
            if response.status_code != 200:
                print(f"Erro ao acessar o link: {response.status_code} - {response.reason}")
                return False

            # Verificar o cabeçalho Content-Type
            content_type = response.headers.get('Content-Type', '')
            if 'xml' not in content_type.lower():
                # messagebox.showinfo(f"O conteúdo não é XML"," Não foi possível carregar os dados!")

                return False

            # Verificar se o conteúdo retornado é XML bem formado
            try:
                ET.fromstring(response.content)  # Tenta fazer o parse do XML
                print("O link é válido e o conteúdo é um XML bem formado.")
                return True
            except ET.ParseError as e:
                print(f"O conteúdo retornado não é um XML bem formado. Erro: {e}")
                return False

        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar o link: {e}")

            return False
    def delete_images_and_qrcode(self):

        # Lista todos os arquivos na pasta
        os.makedirs("image_card", exist_ok=True)
        os.makedirs("image_qrcode", exist_ok=True)

        card = os.listdir(os.path.abspath("image_card"))
        qrcode = os.listdir(os.path.abspath("image_qrcode"))

        for image in card:

            path_abs = os.path.join(os.path.abspath("image_card"), image)
            if os.path.isfile(path_abs):
                os.remove(path_abs)

        for code in qrcode:

            path_abs = os.path.join(os.path.abspath("image_qrcode"), code)

            if os.path.isfile(path_abs):
                os.remove(path_abs)


    def new_data_xml(self):
        """
        Substituir o link xml para novos dados
        :return:
        """
        # Quando abrir as configurações, já aparece o caminho do qrcode
        self.link.set(self.entry_url.get())

        if self.is_valid_xml_data(self.link.get()):

            print("A URL é válida e contém dados XML.")


            if self.query_data_xml:
                print(self.query_data_xml())
                update_data_xml = "UPDATE Data SET link = ?"
                self.cursor.execute(update_data_xml, (self.link.get(),))
                delete_clients_table = "DELETE FROM Socios"
                self.cursor.execute(delete_clients_table)
                self.close_sql()
                self.delete_images_and_qrcode()
                self.download_xml()
                self.filter_members()
                self.generate_all_qrcode()
                self.click_function_main_treeview()
                messagebox.showinfo("Dados xml", "Novos dados carregado com sucesso!")

        else:
            messagebox.showinfo(f"Erro", " Não foi possível carregar os dados!")
            print("A URL não é válida ou os dados não são XML.")

    def filter_members(self):
        """
        Transformo o arquivo xml em um dicionário para exibir os dados em uma treeview
        """
        with open("socios.xml", "rb") as list:
            dict_list = xmltodict.parse(list)


        self.list_dict = []  # lista com os dados completo dos clientes
        self.copy_data = [] # lista para salvar dados para pesquisa da treeview (self.search_tree_view)
        for i in dict_list["Socios"]["Socio"]:
            self.list_dict.append(
                [
                    i["socio-number"],
                    i["renew-date"],
                    i["signature-type"],
                    i["name"],
                    i["email"],
                    i["mobile-phone"],
                    i["address"],
                    i['postal-code'],
                    i['country'],
                    i["card-url"],
                ]
            )
            self.copy_data.append([i["socio-number"],i["name"]])
        self.list_dict.sort(key=lambda x: int(x[0]))

        return self.list_dict


    def resource_path(self,relative_path):
        """Função para utilizar na imagem que será empacotada para o executável."""
        try:
            # Quando executado como um executável
            base_path = sys._MEIPASS
        except AttributeError:
            # Quando executado como script Python
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)