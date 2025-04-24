
## Capítulo 13 - Os Quatro Pilares da POO

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        return "Som de animal"

class Cachorro(Animal):
    def falar(self):
        return "Au au"

class Gato(Animal):
    def falar(self):
        return "Miau"

animais = [Cachorro("Rex"), Gato("Mimi")]
for a in animais:
    print(f"{a.nome}: {a.falar()}")