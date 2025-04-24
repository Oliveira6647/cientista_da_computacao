
## Capítulo 15 - Juntando Tudo - Jogo de Cartas

import random

class Carta:
    def __init__(self, valor):
        self.valor = valor

class Baralho:
    def __init__(self):
        self.cartas = [Carta(i) for i in range(1, 14)] * 4
        random.shuffle(self.cartas)

    def distribuir(self):
        return self.cartas.pop()

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.carta = None

    def jogar(self, baralho):
        self.carta = baralho.distribuir()

class Jogo:
    def __init__(self):
        self.baralho = Baralho()
        self.jogador1 = Jogador("Alice")
        self.jogador2 = Jogador("Bob")

    def iniciar(self):
        self.jogador1.jogar(self.baralho)
        self.jogador2.jogar(self.baralho)
        print(f"{self.jogador1.nome} tirou {self.jogador1.carta.valor}")
        print(f"{self.jogador2.nome} tirou {self.jogador2.carta.valor}")

        if self.jogador1.carta.valor > self.jogador2.carta.valor:
            print(f"{self.jogador1.nome} venceu!")
        elif self.jogador2.carta.valor > self.jogador1.carta.valor:
            print(f"{self.jogador2.nome} venceu!")
        else:
            print("Empate!")

jogo = Jogo()
jogo.iniciar()


