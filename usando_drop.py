import pandas as pd

#Importação dos dados
df = pd.read_csv('/home/oliveira/Downloads/Python Para Data Science/codigo/cap_07/transportes.csv')
print('Antes da alteração')
print(df)
print('Excluído as linhas 3 e 5')
df = df.drop([3, 5])
print(df)
print('Excluíndo a coluna Autonomia')
df =  df.drop('Autonomia', axis=1)
print(df)
print('Excluíndo duas colunas pelo nome')
df = df.drop(['Peso', 'Consumo'], axis=1)
print(df)
