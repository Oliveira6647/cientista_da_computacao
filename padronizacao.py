import pandas as pd
from sklearn.preprocessing import StandardScaler

# Carrega os dados
df = pd.read_csv('/home/oliveira/Downloads/Python Para Data Science/codigo/cap_13/diabetes_preprocessado.csv',
                 names=['#Gravidezes', 'Glicose', 'PD', 'DobraTriceps', 'Insulina', 'IMC',
                        'DiabetesPedigreeFunction', 'Idade', 'Classe'])

#Seleção dos atributos
#Variáveis independentes
X = df.drop('Classe', axis=1)
y  = df['Classe']

#Padronização dos dados
escalonador = StandardScaler()
X = escalonador.fit_transform(X)
df_X = pd.DataFrame(X)
print(df_X)