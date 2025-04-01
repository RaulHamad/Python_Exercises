#refaze rexercicio 51, lendo primeiro termo,
#  a razao e mostrando os 10 primeiros termos usando while


primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
contador = 0
numero_de_termos = primeiro_termo - razao

while contador < 10:
    numero_de_termos += + razao
    contador +=1
    print(numero_de_termos)



