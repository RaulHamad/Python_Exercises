class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
    def get_nome(self):
        return self.__nome
    def get_sobrenome(self):
        return self.__sobrenome
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    def identificacao(self):
        return self.__cpf


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf,codigo):
        super().__init__(nome, sobrenome, cpf)
        self.__codigo = codigo
    def identificacao(self):
        return self.__codigo
    
class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf,matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula
    def identificacao(self,):
        return self.__matricula
    
cliente1 = Cliente('raul','hamad','04646684', '1234')
funcio1 = Funcionario('toto','tata','0222284', '1567')
print(cliente1.nome_completo())
print(cliente1.identificacao())
print(funcio1.identificacao())
print(funcio1.nome_completo())
