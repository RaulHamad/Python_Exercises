#leia um numero inteiro, peça para escolher a opcao que sera:
#1 binario 2 octal 3 hexadecimal

numero = int(input('digite um numero: '))
print(' escolha as opções abaixo: ')
print('[1] binário')
print('[2] octal')
print('[3] hexadecimal')
opcao = int(input('escolha sua opção: '))

if opcao == 1:
    print(' o numero binario de {} é {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print(' o numero octal de {} é {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print(' o numero hexadecimal de {} é {}'.format(numero, hex(numero)[2:]))
else:
    print('opcao invalida')
