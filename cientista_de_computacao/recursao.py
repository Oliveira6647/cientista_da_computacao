#Recursão

#5! = 5 * 4 * 3 * 2 * 1

#Aqui está um algoritmo iterativo que calcula o fatorial de um número, n:

def factorial(n):
    the_product = 1
    while n > 0:
        the_product *= n
        n = n - 1
    return the_product

print(factorial(5))

#Veja como escrever o mesmo algoritmo recursivamente:

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(3))