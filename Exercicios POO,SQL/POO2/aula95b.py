class Pessoa:
    def __init__(self,nome,sobrenome,cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def get_nome(self):
        return f'{self.__nome}'
    def get_sobrenome(self):
        return f'{self.__sobrenome}'
    def get_cpf(self):
        return f'{self.__cpf}'
    def nome_completo(self):
        return f' {self.__nome} {self.__sobrenome}'
    
class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf,renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda

    def get_renda(self):
        return f'{self.__renda}'
    
class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def get_matricula(self):
        return f'{self.__matricula }'
    
cliente1 = Cliente('Jose','Silva','123.345.567-90', 5000)
funcionario1 = Funcionario('Pedro','Souza','999.999.888-70', '2345-90')

print(cliente1.get_nome())
print(funcionario1.get_nome())
print(cliente1.nome_completo())
print(funcionario1.nome_completo())
print(cliente1.get_renda())
print(funcionario1.get_matricula())

