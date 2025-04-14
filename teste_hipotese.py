import pandas as pd
import numpy as np
from scipy.stats   import shapiro

# Carrega os dados
df = pd.read_csv('/home/oliveira/Downloads/Python Para Data Science/codigo/cap_13/diabetes_preprocessado.csv',
                 names=['#Gravidezes', 'Glicose', 'PD', 'DobraTriceps', 'Insulina', 'IMC',
                        'DiabetesPedigreeFunction', 'Idade', 'Classe'])
stat, p = shapiro(df['PD'])
print(f'Estatística={stat:.3f}, p={p:.3f}')
alfa = 0.05   #Nível de significância
if p > alfa:
    print('Não  é possível rejeitar  a hipótese nula (PD segue uma Distribuição Normal)')
else:
    print('Hipotese  nula rejeitada (PD  NÃO  segue uma Distribuição Normal')

stat, p = shapiro(df['IMC'])
print(f'Estatistica={stat:.3f}, p={p:.3f}')
if  p > alfa:
    print('Não é possível rejeitar a hipótese nula (IMC segue uma Distribuição Normal')
else:
    print('Hipótese num rejeitada (IMC NÃO segue uma Distribuição Normal')