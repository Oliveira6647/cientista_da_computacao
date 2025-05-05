#Usando o função bisect left

from bisect import bisect_left




#
 #sorted_fruit = ['apple', 'banana', 'orange', 'plun']
# print(bisect_left(sorted_fruit, 'banana'))

#Se o item que você está procurando não estiver em seu iterável ordenado, bisect_left
#retornará onde ele estaria se estivesse presente

#print(bisect_left(sorted_fruit, 'kiwi'))

#Como você pode ver, 'kiwi' não está em seu iterável ordenado, mas se  estivesse, ocuparia o índice 2

#Já que o bisect_left informa onde um item deveria estar caso não esteja presente, para verificar se um item encontra
#em um iterável, você precisa ver se o índice existe dentro do iterável (bisect poderia retornar uma posição fora do
#iterável) e se o item do índice retornado  por bisect_left é o valor procurado.

#Veja como usar bisect_left para executar uma busca binária em Python:

lista = [1, 3, 5, 7, 9]

def binary_search(an_iterable, target):
    index = bisect_left(an_iterable, target)
    if index <= len(an_iterable) and  an_iterable[index] == target:
        return True
    return  False

print(binary_search(lista, 5))
print(binary_search(lista, 6))
