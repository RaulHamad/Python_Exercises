import random

numero_aleatorio = random.randint(0,5)
numero_chute = int(input('chute um numero entre 0 e 5: '))
if numero_chute == numero_aleatorio:
    print('vc acertou')
else:
    print('vc errou')