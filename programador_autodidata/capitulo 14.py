
## Capítulo 14 - Mais sobre POO

class Pessoa:
    total_pessoas = 0

    def __init__(self, nome):
        self.nome = nome
        Pessoa.total_pessoas += 1

    def __str__(self):
        return f"Pessoa: {self.nome}"

p1 = Pessoa("Lucas")
p2 = Pessoa("Lia")
print(Pessoa.total_pessoas)
print(p1)
