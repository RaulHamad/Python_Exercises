import random

# Jogo da forca

# palco da forca


palco = ['', 'O', 'O-', 'O-|', 'O-|-', 'O-|-<']


class Forca:

    # Método constutor

    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_certas = []

    # Método para adivinhar a letra
    def advinha(self, letra):
        if letra in self.palavra and letra not in self.letras_certas:
            self.letras_certas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True

    # Método para verificar se o jogo terminou
    def forca_acabou(self):
        if self.forca_venceu() or len(self.letras_erradas) >= 5:
            return True
        return False

    # Método para verificar se o jogador venceu

    def forca_venceu(self):
        if '_' not in self.palavra_escondida():
            return True
        return False

    # Método para não mostrar a letra no palco

    def palavra_escondida(self):
        status = ''
        for letra in self.palavra:
            if letra not in self.letras_certas:
                status += '_'
            else:
                status += letra
        return status

    # Método para checar o status do jogo e imprimir o palco na tela

    def mostra_status(self):

        print('\n===== Jogo da Forca =====')
        print(palco[len(self.letras_erradas)])
        print(f'Palavra: {self.palavra_escondida()}')
        print('\n Letras Erradas')
        for letra in self.letras_erradas:
            print(letra,)
        print('\n Letras Certas')
        for letra in self.letras_certas:
            print(letra,)


# Função para ler uma palavra aleatória do banco de palavras


def palavra_aleatoria():
    with open("palavras.txt", 'rt') as f:
        banco = f.readlines()
    return banco[random.randint(0, len(banco))].strip()


# Função main que executa o programa


def main():
    # Objeto
    jogo = Forca(palavra_aleatoria())

    # Enquanto o jogo não tiver terminado, mostrar do status,
    # Solicita uma letra e faz a leitura do caracter
    while not jogo.forca_acabou():
        jogo.mostra_status()
        letra_escolhida = input('\n Digite uma letra: ')
        jogo.advinha(letra_escolhida)

    # Verifica o status do jogo
    jogo.mostra_status()

    # De acordo com o status, imprime mensagem na tela para o usuario
    if jogo.forca_venceu():
        print('\nParbéns!! Você venceu!!')
    else:
        print('\n Final do Jogo, Você PERDEU')
        print(f'\n A palavra era {jogo.palavra}')

    print('THE END!')

# Executar o programa
if __name__ == "__main__":
    main()
