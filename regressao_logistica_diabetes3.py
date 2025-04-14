import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport  # <- Importação correta

# Carrega os dados
df = pd.read_csv('/home/oliveira/Downloads/Python Para Data Science/codigo/cap_13/diabetes_preprocessado.csv',
                 names=['#Gravidezes', 'Glicose', 'PD', 'DobraTriceps', 'Insulina', 'IMC',
                        'DiabetesPedigreeFunction', 'Idade', 'Classe'])

# Cria o relatório
relatorio = ProfileReport(df, title="Relatório Diabetes", explorative=True)

# Salva o relatório como HTML
relatorio.to_file("/home/oliveira/Downloads/relatorio_diabetes.html")
