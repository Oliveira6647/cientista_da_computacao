#Algoritmo de Euclides em Python:

def gcf(x, y):
    while y != 0:
        x, y = y, x % y
    return x

# Teste com print
resultado = gcf(20, 12)
print(f"O máximo divisor comum entre 20 e 12 é: {resultado}")

