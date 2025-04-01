#ler um valor de salario e aumentar 15%

salario_normal = float(input('digitar salario: '))
salario_aumento = salario_normal + (salario_normal * (15/100))
print('seu salario é {} e com aumento de 15% fica {}'.format(salario_normal, salario_aumento))