import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv('/home/oliveira/Downloads/Python Para Data Science/codigo/cap_13/diabetes_preprocessado.csv', \
                 names=['#Gravidezes', 'Glicose', 'PD', 'DobraTriceps', 'Insulina', 'IMC', \
                        'DiabetesPedigreeFunction', 'Idade', 'Classe'])
df_classe = pd.DataFrame({
    'classe':['Sem Diabetes', 'Com Diabetes'],
    'quantidade':[len(df[df['Classe'] == 0]), len(df[df['Classe'] == 1])]
})

df_classe.plot(kind='bar', x='classe', y='quantidade')

