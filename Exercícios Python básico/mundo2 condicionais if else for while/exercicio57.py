#programa q leia o sexo de uma pessoa mas so aceite valores 'M' ou 'F'
#caso esteja errado peça para digitar novamente


sexo = input('Digite seu sexo M/F: ').upper().strip()[0]
while sexo not in 'M' 'F':
    print('comando invalido, tente outra vez')
    sexo = input('Digite seu sexo M/F: ').upper().strip()[0]

print('dado armazenado com sucesso')