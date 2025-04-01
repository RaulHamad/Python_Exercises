class Animal:
    def __init__(self,nome):
        self.__nome = nome
        
    def get_nome(self):
        return self.__nome
    def cumprimentar(self):
        return f'Eu sou {self.__nome}'
    
class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def andar(self):
        return f'{super().get_nome()} Andando pela terra'
    def cumprimentar(self):
        return f'Olá jovem, sou {super().get_nome()} da terra'
    
class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    def nadar(self):
        return f'{super().get_nome()} Nadando por ai'
    def cumprimentar(self):
        return f'Olá velho, sou {super().get_nome()} da água'
class Pinguim(Terrestre,Aquatico):
    def __init__(self, nome):
        super().__init__(nome)

jabuti = Terrestre('totuig')
print(jabuti.andar())
print(jabuti.cumprimentar())
print('------')
golfinho = Aquatico('flipper')
print(golfinho.nadar())
print(golfinho.cumprimentar())
print('------')
pinguim = Pinguim('capitao')
print(pinguim.nadar())
print(pinguim.andar())
print(pinguim.cumprimentar())