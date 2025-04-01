class automovel:
    def __init__(self, placa, velocidade_max):
        self.__placa = placa
        self.__velocidade_max = velocidade_max
        self.__velocidade_atual = 0

    def __str__(self):
        return f'velocidade inicial a {self.__velocidade_atual}km/h'

    def get_placa(self):
        return self.__placa

    def dirigir(self, velocidade):
        print(f'Estou dirigindo a {velocidade} km/h')

    def acelerar(self):
        maxima = self.__velocidade_max
        nova = self.__velocidade_atual + 10
        self.__velocidade_atual = nova if nova <= maxima else maxima

    def frear(self):
        nova = self.__velocidade_atual - 10
        self.__velocidade_atual = nova if nova >= 0 else 0


meu_carro = automovel('xy0011', 180)

print(meu_carro)
print(meu_carro.__velocidade_max)
print(meu_carro.get_placa())

#violação do principio de encapsulamento
meu_carro.__placa = 'xxx0000'
meu_carro.__velocidade_max = 1000
meu_carro.__velocidade_atual = 200

print(meu_carro)
print(meu_carro.__velocidade_max)
print(meu_carro.get_placa())