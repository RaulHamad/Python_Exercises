import time

def menu(txt):
    print('-'*45)
    print(txt.center(45))
    print('-'*45)
    


def cadastro():

    return 'Ver pessoas cadastradas'
    

def cadastros_opcoes():
    print('-'*45)
    print(f'\t{cadastro()}')
    print('-'*45)
    return

def cadastrar():

    return 'Cadastrar nova Pessoa'
    

def cadastrar_pessoas():
    print('-'*45)
    print(f'\t{cadastrar()}')
    print('-'*45)
    return

def sair_sistema():
    return 'Sair do Sistema'
    

def fechando_sistema():
    print('-'*45)
    print('\t\tFinalizando Sistema')
    print('-'*45)

def lista_opções():
    for c in range(0,3):
        if c == 0:
            print(f'{c+1} - {cadastro()}')
        if c == 1:
            print(f'{c+1} - {cadastrar()}')
        if c == 2:
            print(f'{c+1} - {sair_sistema()}')
    
def opcoes():
    while True:
        try:
        
            opcao = int(input('Sua Opção: '))
                            
        except:
            print(f'\033[0;31mOpção invalida...\033[m')
            time.sleep(2)
            print(menu('Menu Principal'))
            print(lista_opções())
        else:

            if opcao == 1:
                print(cadastros_opcoes())
            elif opcao == 2:
                print(cadastrar_pessoas())
            elif opcao == 3:
                print(fechando_sistema())
                break
            else:
                print(f'\033[0;31mOpção invalida...\033[m')
                time.sleep(2)
                print(menu('Menu Principal'))
                print(lista_opções())
        