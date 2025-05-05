#Tempo  exponencial

pin = 931
n = len(str(pin))
for i in range(10**n):
    if i == pin:
        print(i)
        