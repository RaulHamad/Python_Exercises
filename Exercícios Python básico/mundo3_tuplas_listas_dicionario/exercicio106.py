#faça um mini sistema que utiliza o interactive help do python.
#O usuario vai digitar o comando e o manual vai aparecer.
#quando o usuario digitar a palavra "fim" o programa se encerrará.
#obs.: use cores

print('=' *20)
print('Exercicio 106')
print('=' *20)

def interactiveHelp():
    import time
    print('\033[1;31;40m~'* 33)
    print('  Bem vindo ao Interactive Help')
    print('\033[1;31;40m~\033[m'* 33)
    time.sleep(0.5)
    
    while True:
        a = input('\033[0;0;43mFunção ou Biblioteca>: \033[m')
        print(f'\033[0;30;45mCarregando comando {a}...')
        time.sleep(1)
        
        print(help(a))
        
        continuar = input('\033[mDeseja continuar["fim" para encerrar]: ').strip().lower()
        while continuar != 's' and continuar != 'fim':
            print('Comando inválido...')
            continuar = input('Deseja continuar["fim" para encerrar]: ').strip().lower()
        if continuar == 'fim':
            break        
    



interactiveHelp()

