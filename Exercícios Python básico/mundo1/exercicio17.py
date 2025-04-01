#ler um numero para o cateto adjacente e cateto oposto. retorne a hipotenusa
import math
cateto_oposto = float(input('digite a cateto oposto: '))
cateto_adjacente = float(input('digite a cateto adjacente: '))
hipotenusa = math.hypot(cateto_adjacente, cateto_oposto)
print(hipotenusa)