
# ---------------------- Capítulo 7: Loops ----------------------

# Loop for
for i in range(5):
    print(f"Número {i}")

# Função range
for i in range(1, 11):
    print(i * 2)

# Loop while
contador = 0
while contador < 3:
    print("Contando", contador)
    contador += 1

# Instrução break
for letra in "Python":
    if letra == "h":
        break
    print(letra)

# Instrução continue
for letra in "Python":
    if letra == "h":
        continue
    print(letra)

# Loops aninhados
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")

# Desafio
soma = 0
for numero in range(1, 6):
    soma += numero
print(f"Soma dos números de 1 a 5: {soma}")
