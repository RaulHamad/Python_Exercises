#crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso
#de zero ate vinte. seu programa devera ler um numero
#  pelo teclado(entre 0 e 20) e mostra-lo por extenso.

print('=' *20)
print('Exercicio 72')
print('=' *20)

num_extenso = ('zero', 'um', 'dois', 'tres', 'quatro',
 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
  'doze', 'treze', 'catorze', 'quinze', 'dezesseis', ' dezesete',
   'dezoito', ' dezenove', 'vinte')

continuar = 'L'
num_usuario = int(input('Digite um numero entre 0 e 20: '))
while True:
    if  0 <= num_usuario <= 20:
        print(f'voce digitou {num_extenso[num_usuario]}')
        break
    else:
        num_usuario = int(input('Opção inválida...Digite um numero entre 0 e 20: '))
while continuar not in 'SN':
    continuar = input('Deseja continuar [S/N]: ').strip().upper()[0]
    while continuar == 'S':
        num_usuario = int(input('Digite um numero entre 0 e 20: '))
        while True:
            if  0 <= num_usuario <= 20:
                print(f'voce digitou {num_extenso[num_usuario]}')
                break
            else:
                num_usuario = int(input('Opção inválida...Digite um numero entre 0 e 20: '))
        continuar = input('Deseja continuar [S/N]: ').strip().upper()[0]
print('Finalizando programa...')
            


