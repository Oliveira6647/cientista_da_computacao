# _*_ coding: utf-8 _*_
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

# Leitura do dataset
dataset = pd.read_csv('/home/oliveira/Downloads/Python Para Data Science/codigo/cap_07/tempo_salarios.csv')
X = dataset.iloc[:, 0].values
y = dataset.iloc[:, 1].values

# Converte para arrays 2D
X = X.reshape(-1, 1)
y = y.reshape(-1, 1)

# Padronização dos dados
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

# SVR com kernel linear
regressor_linear = SVR(kernel='linear')
y_ravel = np.ravel(y)  # SVR precisa de y como 1D
regressor_linear.fit(X, y_ravel)

# Plot regressão linear
plt.figure(dpi=170)
plt.scatter(sc_X.inverse_transform(X), sc_y.inverse_transform(y), color='red')
plt.plot(sc_X.inverse_transform(X),
         sc_y.inverse_transform(regressor_linear.predict(X).reshape(-1, 1)),
         color='blue')
plt.title('Regressão Linear usando SVR - kernel Linear')
plt.xlabel('Anos de Experiência')
plt.ylabel('Salário')
plt.show()

# SVR com kernel RBF
regressor_rbf = SVR(kernel='rbf')
y_ravel = np.ravel(y)  # Garante que y esteja no formato certo
regressor_rbf.fit(X, y_ravel)

# Plot regressão RBF
plt.figure(dpi=170)
plt.scatter(sc_X.inverse_transform(X), sc_y.inverse_transform(y), color='red')
plt.plot(sc_X.inverse_transform(X),
         sc_y.inverse_transform(regressor_rbf.predict(X).reshape(-1, 1)),
         color='blue')
plt.title('Regressão usando SVR - kernel RBF')
plt.xlabel('Anos de Experiência')
plt.ylabel('Salário')
plt.show()
