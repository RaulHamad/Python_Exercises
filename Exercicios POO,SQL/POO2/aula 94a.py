from passlib.hash import pbkdf2_sha256 as cryp


class usuario:
    def __init__(self,nome,sobrenome,email,senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=1000, salt_size=10)

    def nome_completo(self):
        return f'Seu nome é {self.__nome} {self.__sobrenome} e email {self.__email}'
    def checa_senha(self,senha):
        if cryp.verify(senha,self.__senha):
            return True
        
novo_usuario = usuario('raul','hamad','toto@','1234')
print(novo_usuario.nome_completo())

while True:
    nome = input('Digite nome: ')
    sobrenome = input('Digite sobrenome: ')
    email = input('Digite email: ')
    senha = input('Digite senha: ')
    conferir_senha = input('confirme senha: ')
    if senha == conferir_senha:
        user = usuario(nome,sobrenome,email,senha)
        break
    else:
        print('as senha nao conferem')
print('cadastro completo')
senha = input('informe a senha: ')
if user.checa_senha(senha):
    print(f'Logado com sucesso')
else:
    print(f'acesso negado')
