#crie um programa que tenha a funcao leiaInt() qua vai 
#funcionar de forma semelhante a função input() do python,
# so que fazendo a validação para aceitar apenas
# um valor numerico.

print('=' *20)
print('Exercicio 104')
print('=' *20)


def leiaInt(a):
    while True:
        a = input('Digite um numero inteiro: ')
        if a.isnumeric():
            return a
            
        else:
            print('\033[31m O que foi digitado não é um numero inteiro \033[m')
            
               

        
n=leiaInt('Digite um numero inteiro:')
print(f'Voçê digitou o numero {n}')