import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

df = pd.read_csv('/home/oliveira/Downloads/Python Para Data Science/codigo/cap_13/diabetes_preprocessado.csv', \
                 names = ['#Gravidezes', 'Glicose', 'PD', \
                          'DobraTriceps', 'Insulina', 'IMC',  \
                          'DiabetesPedigreeFunction', 'Idade', \
                          'Classe'])
scatter_matrix(df, figsize=(15,8))
plt.show()