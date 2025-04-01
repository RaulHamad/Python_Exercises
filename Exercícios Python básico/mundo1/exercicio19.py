#sortear um nome dentre 4 alunos

import random

alunos = ['raul', 'matheus', 'lucas', 'thais']
sorteado = random.choice(alunos)
random.shuffle(alunos)

print(sorteado)
print(alunos)

