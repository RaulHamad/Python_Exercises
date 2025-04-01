class Livro:
    def __init__(self,titulo,autor,editora,ano,quantidade):
        self.__titulo = titulo
        self.__autor = autor
        self.__editora = editora
        self.__ano = ano
        self.__quantidade = quantidade
    
    def __repr__(self) -> str:
        return self.__titulo
    
    def __str__(self):
        return self.__autor
    
    def __len__(self):
        return self.__quantidade
    
    def __add__(self,other):
        return self.__quantidade + other.__quantidade
    
    def __del__(self):
        print(f'Encerrando o programa e deletado')


livro1 = Livro('Pokemon filme', 'Satoru', 'Movie Star',1999,500)
livro2 = Livro('Vampiro a Mascara','Makunouchi','Toto editora',1995,50 )

print(livro1)
print(livro2)
print(livro1.__len__())
print(livro1+livro2)
