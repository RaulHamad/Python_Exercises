#reescreva a função leiaInt() que fizemos no desafio 104 incluindo a possibilidade
#da digitação de um numero de tipo invalido. aproveite e crie a função leiaFloat
# com a mesma funcionalidade.

def leiaInt():

    while True:
        try:
            num = int(input('Digite um numero Inteiro: '))

        except(ValueError,TypeError):
            print('\033[0;31mO dado digitado não é válido\033[m')
        except(KeyboardInterrupt):
            print('O usuario finalizou o programa')
            return 0        
        else:
            return num
            

def leiaFloat():

    while True:
        try:
            num = float(input('Digite um numero Real: '))
        except(ValueError,TypeError):
            print('\033[0;31mO dado digitado não é válido\033[m')
        except(KeyboardInterrupt):
            print('O usuario finalizou o programa')
            return 0        
        else:
            return num
            



n= leiaInt()
m= leiaFloat()
print(f'O numero inteiro foi {n} e o numero real foi {m}')

