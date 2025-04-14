import pandas as pd
import matplotlib.pyplot as  plt

EIXO_LINHAS = 0
EIXO_COLUNAS = 1

dados = pd.read_csv('/home/oliveira/Downloads/Python Para Data Science/codigo/cap_13/vendas.csv')
compradores = dados[dados['Comprou']==1]
compradores.drop(['Comprou'], axis=EIXO_COLUNAS)

plt.title('Compras por idade e Renda')
plt.xlabel('Renda Anual x 1000 (R$)')
plt.ylabel('Idade (Anos)')
plt.scatter(compradores.Renda/1000, compradores.Idade, s=2)
print(plt.show())
