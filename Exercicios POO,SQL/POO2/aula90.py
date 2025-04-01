class automovel:
    def __init__(self, placa, velocidade_max):
        self.placa = placa
        self.velocidade_max = velocidade_max
        self.velocidade_atual = 0

    def __str__(self):
        return f'velocidade inicial a {self.velocidade_atual}km/h'

    def get_placa(self):
        return self.placa

    def dirigir(self, velocidade):
        print(f'Estou dirigindo a {velocidade} km/h')

    def acelerar(self):
        maxima = self.velocidade_max
        nova = self.velocidade_atual + 10
        self.velocidade_atual = nova if nova <= maxima else maxima

    def frear(self):
        nova = self.velocidade_atual - 10
        self.velocidade_atual = nova if nova >= 0 else 0


meu_carro = automovel('xy0011', 150)

print(meu_carro.get_placa())
print(meu_carro.__str__())
meu_carro.dirigir(50)

for _ in range(20):
    meu_carro.acelerar()
    print(meu_carro)
for _ in range(20):
    meu_carro.frear()
    print(meu_carro)