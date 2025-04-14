#  _*_ coding uff-8 _*_
#Regressão Polinomial

#Importando os módulos das bibliotecas
import matplotlib.pyplot as plt
import  pandas as pd
#Dividindo o dataset entre  treino e teste
from sklearn.model_selection import train_test_split
#Ajustando o modelo de Regressão linear Regression
from sklearn.linear_model import LinearRegression
#Criando o modelo de Regressão Polinomial - grau 4
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import cross_val_score

#Carregando o dataset
dataset = pd.read_csv('/home/oliveira/Downloads/Python Para Data Science/codigo/cap_11/cargo_nivel_salarios.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
lin_reg = LinearRegression()
lin_reg.fit(X, y)

#Ajustando e plotando o modelo para o grau 12
poly_reg = PolynomialFeatures(degree=12)

#Ajustando o modelo para os dados de treino
# X_poly = poly_reg.fit_transform((X_train))
# poly_reg.fit(X_poly, y_train)
# poly_reg.fit(X_train, y_train)
# lin_reg_2 = LinearRegression()
# lin_reg_2.fit(X_poly, y_train)

#Ajustando o modelo para todos os dados
X_poly = poly_reg.fit_transform(X)
poly_reg.fit(X_poly, y)
poly_reg.fit(X, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)


#Visualizar os resultado de treino
# plt.figure(figsize=(15,8))
# plt.plot(X_train, y_train, 'Dr')
# plt.plot(X_train,  lin_reg_2.predict(poly_reg.fit_transform(X_train)),  '^b')
# plt.title('Nível x Salário (Regressão Polynomial')
# plt.xlabel('Nível')
# plt.ylabel('Salário')
# print(plt.show())

#Visualizar os resultado de teste
# plt.figure(figsize=(15,8))
# plt.plot(X_test, y_test, 'Dr')
# plt.plot(X_test, lin_reg_2.predict(poly_reg.fit_transform(X_test)), '^b')
# plt.title('Nível x Salários (Regressão Polinomial)')
# plt.xlabel('Nível')
# plt.ylabel('Salário')
# print(plt.show())

#Visualizar com todas as amostras
plt.figure(figsize=(15,8))
plt.plot(X, y, 'Dr')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), '^b--')
plt.title('Nível x Salário  (Regressão Polinomial)')
plt.xlabel('Nível')
plt.ylabel('Salário')
print(plt.show())



# plt.plot(X,   y , 'Dr')
# plt.plot(X, lin_reg.predict(X), 'b-')
# plt.title('Nível x Salário   (regressão linear) ')
# plt.xlabel('Nível')
# plt.ylabel('Salário')
# print(plt.show())
