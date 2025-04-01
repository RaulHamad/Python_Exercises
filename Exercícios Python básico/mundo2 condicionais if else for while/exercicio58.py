#computador pensa em um numero entre 0 e 10
#o jogador tenta adivinhar e o programa
#  vai mostrando no final quantos palpites foram necessarios para vencer
import random

numero_computador = random.randint(0,10)
palpite = int(input('adivinhe um numero entre 0 e 10: '))
contador = 1
while palpite != numero_computador:
    if palpite > numero_computador:
        contador += 1
        print('chute um numero mais baixo')
        palpite = int(input('adivinhe um numero entre 0 e 10: '))
    if palpite < numero_computador:
        contador += 1
        print('chute um numero mais alto')
        palpite = int(input('adivinhe um numero entre 0 e 10: '))
print('voce acertou')
print('voce fez {} tentativas para acertar'.format(contador))