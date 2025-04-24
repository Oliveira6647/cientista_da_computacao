# ---------------------- Capítulo 4: Funções ----------------------

# Representação de conceitos por funções

def saudacao(nome):
    """Exibe uma saudação personalizada"""
    return f"Olá, {nome}!"

print(saudacao("Márcio"))

# Reutilização de funções

def quadrado(numero):
    return numero ** 2

print(quadrado(4))

# Parâmetros obrigatórios e opcionais

def apresentar(nome, idade=30):
    print(f"Nome: {nome}, Idade: {idade}")

apresentar("Joana")

# Escopo
mensagem_global = "Olá!"

def mostrar():
    mensagem_local = "Bem-vindo"
    print(mensagem_global)

mostrar()
# print(mensagem_local) # erro: variável fora do escopo

# Manipulação e exceções
try:
    numero = int("abc")
except ValueError:
    print("Erro de conversão")

# Docstrings já mostrada acima em 'saudacao'

# Só use uma variável quando necessário: evite variáveis desnecessárias

# Desafio

def calcular_area(base, altura):
    return base * altura

print("Área do retângulo:", calcular_area(5, 3))