#crie um programa que leia dois valores e mostre um menu na tela~
#[1] somar [2]multiplicar [3] maior [4] novos numeros [5]sair do programa
#seu programa devera realizar a operacao solicitada em casa caso

numero_1 = float(input('digite um numero: '))
numero_2 = float(input('digite outro numero: '))

opcao = 0

while opcao != '5':
    print('[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos Numeros \n[5] Sair')
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        print('Sua opção foi a somar {} e {} que é igual a {}'.format(numero_1, numero_2,(numero_1 + numero_2)))
    elif opcao == '2':
        print('Sua opção foi a multiplicar {} e {} que é igual a {}'.format(numero_1, numero_2,(numero_1 * numero_2)))
        
    elif opcao == '3':
        if numero_1 > numero_2:
            print('Sua opção foi saber o numero maior entre {} e {} que é o numero {}'.format(numero_1, numero_2,numero_1))
            
        elif numero_2 > numero_1:
            print('Sua opção foi saber o numero maior entre {} e {} que é o numero {}'.format(numero_1, numero_2,numero_2))
            
        else:
            print('Sua opção foi saber o numero maior entre {} e {}. Ambos são iguais'.format(numero_1, numero_2))
            
    elif opcao == '4':
        numero_1 = float(input('digite um numero: '))
        numero_2 = float(input('digite outro numero: '))
        
    else:
        print('opção invalida, digite novamente')
        
print('programa finalizado')


