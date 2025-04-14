#Importação das bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from patsy.state import center

#Importação dos dados
df = pd.read_csv('/home/oliveira/Downloads/Python Para Data Science/codigo/cap_13/diabetes.csv',\
                 names=['#Gravidezes', 'Glicose',
                        'PD','DobraTriceps', 'Insulina', 'IMC',
                        'DiabetesPedigreeFunction', 'Idade', 'Classe'])
print('Estatísticas Descritivas')
print(df.describe())
print('\nContando os zeros na amostra: \n')
print(f'Números de gravidezes: {(df["#Gravidezes"]==0).sum()}')
print(f'Glicose:  {(df["Glicose"]==0).sum()}')
print(f'Pressão diastótica: {(df["PD"]==0).sum()}')
print(f'Espessura da dobra do tríceps:   {(df["DobraTriceps"]==0).sum()}')
print(f'Insulina: {(df["Insulina"]==0).sum()}')
print(f'IMC: {(df["IMC"]==0).sum()}')
print(f'Idade: {(df["Idade"]==0).sum()}')