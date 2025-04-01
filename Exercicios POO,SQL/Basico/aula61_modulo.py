def pega_sobrenome():
    sobrenome = input('Digite seu nome: ')
    while True:
        if sobrenome:
            if sobrenome.isalpha():
                return sobrenome
            else:
                print('Digite um sobrenome válido')
                sobrenome = input('Digite seu nome: ')
        else:
            return sobrenome

def pega_idade():
    
    while True:
        try:
            idade = int(input('Qual sua idade: '))
        except:
            print('Digite uma idade válida')
            
        else:
            if idade:
                return idade
            else:
                print('Digite uma idade válida')

def pega_altura():
    while True:
        try:
            altura = int(input('Sua altua em cm: '))
        except:
            print('Digite uma altura valida')
        else:
            if altura:
                return altura
            else:
                print('Digite altura valida')

def pega_peso():
    while True:
        try:
            peso = int(input('Seu peso em kg: '))
        except:
            print('Digite um  peso valido')
        else:
            if peso:
                return peso
            else:
                print('Digite um  peso valido')