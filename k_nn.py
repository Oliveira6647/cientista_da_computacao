import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

# Carregar dados
df = pd.read_csv('/home/oliveira/Downloads/Python Para Data Science/codigo/cap_16/bank_note.csv')
print(df.shape)
print(df.head())

# Separar variáveis independentes e dependente
X = df.iloc[:, 0:4].values
y = df.iloc[:, 4].values

# Dividir em treino e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=3)

# Escalonamento
escalonador = StandardScaler()
X_treino = escalonador.fit_transform(X_treino)
X_teste = escalonador.transform(X_teste)

# Algoritmo KNN
algoritmo = KNeighborsClassifier(n_neighbors=3)
algoritmo.fit(X_treino, y_treino)

# Previsões e métricas
previsoes = algoritmo.predict(X_teste)
matriz_confusao = confusion_matrix(y_teste, previsoes)
acuracia = accuracy_score(y_teste, previsoes)

print(f'Matriz de Confusão: \n{matriz_confusao}')
print(f'Acurácia do modelo: {acuracia:.2f}')
