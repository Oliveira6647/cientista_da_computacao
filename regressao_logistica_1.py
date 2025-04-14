import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('/home/oliveira/Downloads/Python Para Data Science/codigo/cap_13/vendas.csv')
X = dados['Idade']  # variável independente
y = dados['Comprou']


plt.title('Comprou por idade')
plt.xlabel('Idade')
plt.ylabel('Comprou')
plt.scatter(X, y, s=2)
print(plt.show())
