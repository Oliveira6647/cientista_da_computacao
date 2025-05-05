#Complexidade de espaço

x = 1
n = 5
for i in range(1, n + 1):
     x = x * i

print(x)

x = 1
n = 5
a_list = []
for i in range(1, n + 1):
    a_list.append(x)
    x = x * i

print(x)