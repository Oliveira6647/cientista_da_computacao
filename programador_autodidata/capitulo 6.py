
# ---------------------- Capítulo 6: Manipulação de Strings ----------------------

# Strings com aspas triplas
texto_longo = """Isso é uma string
com múltiplas linhas."""
print(texto_longo)

# Índices
nome = "Márcio"
print(nome[0])  # imprime 'M'

# Strings são imutáveis
# nome[0] = 'm'  # erro!

# Concatenação
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome
print(nome_completo)

# Multiplicação de strings
print("-" * 10)

# Maiúsculas e minúsculas
print(nome.upper())
print(nome.lower())
print(nome.capitalize())

# Método format
mensagem = "Meu nome é {} e tenho {} anos.".format("Márcio", 45)
print(mensagem)

# Método split
frase = "Aprender Python é divertido"
palavras = frase.split()
print(palavras)

# Método join
juncao = ", ".join(palavras)
print(juncao)

# Remoção de espaços
espacado = "  Olá  "
print(espacado.strip())

# Método replace
print(frase.replace("divertido", "fantástico"))

# Busca de um índice
print(frase.find("Python"))

# Palavra-chave 'in'
print("Python" in frase)

# Escape de strings
print("Ela disse: \"Olá!\"")

# Nova linha
print("Linha 1\nLinha 2")

# Fatiamento
print(nome[0:3])  # 'Már'

# Desafio
email = input("Digite seu email: ").strip()
usuario = email.split("@")[0]
dominio = email.split("@")[1]
print(f"Usuário: {usuario}\nDomínio: {dominio}")
