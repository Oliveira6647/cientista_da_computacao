import pandas as pd

dados = pd.read_csv('/home/oliveira/Downloads/archive (2)/Electric_Vehicle_Population_Data.csv')
print(dados)
print(dados.drop_duplicates())