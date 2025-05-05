#Ordenação por intercalação
from numpy.ma.core import left_shift

a_list = [6, 3, 9, 2]

#Esta parte do algoritmo é responsável por dividir as listas em sublistas:
def merge_sort(a_list):
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

#Esta parte é responsável por intercalar duas listas:
        left_ind = 0
        right_ind = 0
        alist_ind = 0
        while left_ind < len(left_half) and right_ind < len(right_half):
            if left_half[left_ind] <= right_half[right_ind]:
                a_list[alist_ind] = left_half[left_ind]
                left_ind += 1
            else:
                a_list[alist_ind] = right_half[right_ind]
                right_ind  += 1
            alist_ind += 1

        while left_ind < len(left_half):
            a_list[alist_ind] = left_half[left_ind]
            left_ind += 1
            alist_ind += 1

        while right_ind < len(right_half):
            a_list[alist_ind] = right_half[right_ind]
            right_ind += 1
            alist_ind += 1

merge_sort(a_list)
print(a_list)


#Código traduzido para o português
# Ordenação por intercalação (Merge Sort)

lista = [6, 3, 9, 2]

# Esta função divide a lista em sublistas recursivamente
def ordena_intercalacao(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        metade_esquerda = lista[:meio]
        metade_direita = lista[meio:]

        ordena_intercalacao(metade_esquerda)
        ordena_intercalacao(metade_direita)

        # Intercala as duas metades ordenadas
        indice_esq = 0
        indice_dir = 0
        indice_geral = 0

        while indice_esq < len(metade_esquerda) and indice_dir < len(metade_direita):
            if metade_esquerda[indice_esq] <= metade_direita[indice_dir]:
                lista[indice_geral] = metade_esquerda[indice_esq]
                indice_esq += 1
            else:
                lista[indice_geral] = metade_direita[indice_dir]
                indice_dir += 1
            indice_geral += 1

        while indice_esq < len(metade_esquerda):
            lista[indice_geral] = metade_esquerda[indice_esq]
            indice_esq += 1
            indice_geral += 1

        while indice_dir < len(metade_direita):
            lista[indice_geral] = metade_direita[indice_dir]
            indice_dir += 1
            indice_geral += 1

# Executa a ordenação
ordena_intercalacao(lista)
print(lista)



