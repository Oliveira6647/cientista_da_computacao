#Ordenação por bolha

a_list = [32, 1, 9, 6]

#Sua função bubble_sort recebeu uma lista de número chamada a_list como parâmetro:
def bubble_sort(a_list):
    #Dentro da função, você  está obtendo o tamanho da lista, diminuindo 1 e salvando o resultadom em
    #list_length para controlar o número de iterações que  que seu algoritmo executatá:
    list_length = len(a_list) - 1
    #A função tem dois loops aninhados para você percorrer a lista e fazer comparações:
    for i in range(list_length):
        for j in range(list_length):
            #Dentro do loop for  interno, você usou uma instrução  if para comparar o número atual com o número que vem
            #depois dele, adicionando 1 ao índice do número atual:
            #atual ------número seguinte
            if a_list[j] > a_list[j + 1]:
                #Se o número atual for maior do que o número seguinte, você os trocará de posição
                #A sintaxe Python a seguir permite trocar dois itens sem carregar um deles em uma variável temporária:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
    return a_list


print(bubble_sort(a_list))


