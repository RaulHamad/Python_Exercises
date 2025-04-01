#programa q mostra contagem regressiva de 10 a 0 com pausa de 1 segundo entre eles

import time

contador = 10
for c in range(contador,-1,-1):
    time.sleep(1)
    print(c)