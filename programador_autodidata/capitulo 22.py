
# -----------------------------
# CAPÍTULO 22 - ALGORITMOS
# -----------------------------
print("Capítulo 22 - Algoritmos")
# FizzBuzz
for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Palíndromo
palavra = "radar"
print(f"{palavra} é palíndromo?", palavra == palavra[::-1])

# Anagrama
def eh_anagrama(str1, str2):
    return sorted(str1) == sorted(str2)
print("amor e roma são anagramas?", eh_anagrama("amor", "roma"))

# Contagem de caracteres
from collections import Counter
print(Counter("banana"))

# Recursão - fatorial

def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n-1)

print("Fatorial de 5:", fatorial(5))
