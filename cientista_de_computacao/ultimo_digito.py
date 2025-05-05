#sintaxe de uma compreensão de lista

#new_list = [expression[i] for i in iterable if filter(i)]
#iterable é o iterável que você está usando para criar sua nova lista. expression(i) é uma variável que armazena
# cada elemento de iterable. Por  exemplo, nesta expressão regular,
# c  contém cada caractere da string  "selftaught"
print([c for c in "selftaught"])

#filter(i) permite fazer alterações no iterável original. Por exemplo, você pode criar um filtro que só
#adicione itens ao iterável se atenderem aos seus requisitos:

print([c for c in "selftaught" if ord(c) > 102])

s = "Buy 1 get 2 free"
nl = [c for c in  s if c.isdigit()]
print(nl)

#Busca do dígito da  extrema  direita, que é usar um índice negativo para obter o último digito de sua nova lista:
s = "Buy 1 get 2 free"
nl = [c for c in  s if c.isdigit()][-1]
print(nl)

