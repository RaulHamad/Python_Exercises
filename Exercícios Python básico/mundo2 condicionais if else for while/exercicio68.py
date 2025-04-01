print('=-=' * 10)
print('helo world')
print('Exercicio68')
print('=-=' * 10)
from random import randint


contador = 0
while True:
    num_pc = randint(0,10)
    num_jogador = int(input('escolha um numero: '))
    escolha_jogador = input('Escolha Par ou Ímpar [P/I]: ').strip().upper()
    contador += 1
    while escolha_jogador not in 'PI':
        escolha_jogador = input('Escolha Par ou Ímpar [P/I]: ').strip().upper()
    if escolha_jogador == 'P':
        if (num_jogador + num_pc) % 2 == 0:
            print(f'voce jogou {num_jogador} e o computador {num_pc}')
            print('voce venceu!!!')
            
        else:
            break
    if escolha_jogador == 'I':
        if (num_jogador + num_pc) % 2 != 0:
            print(f'voce jogou {num_jogador} e o computador {num_pc}')
            print('voce venceu!!!')
            
        else:
            break
            
      
print(f'voce jogou {num_jogador} e o computador {num_pc}')
print(f'{num_pc + num_jogador} é impar, voce Perdeu!!!')
print(f'voce perdeu com {contador} tentativas')