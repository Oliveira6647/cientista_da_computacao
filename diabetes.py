# Importando as bibliotecas principais
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Carregando o dataset de diabetes
df = pd.read_csv('/home/oliveira/Downloads/archive(2)/diabetes.csv')

# Separando as variáveis independentes (X) e a variável alvo (y)
X = df.drop('Outcome', axis=1)  # 'Outcome' indica se o paciente tem diabetes
y = df['Outcome']

# Dividindo os dados em treino e teste (70% treino, 30% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Criando o modelo de Random Forest
modelo = RandomForestClassifier(n_estimators=100, random_state=42)

# Treinando o modelo com os dados de treino
modelo.fit(X_train, y_train)

# Fazendo previsões com os dados de teste
y_pred = modelo.predict(X_test)

# Calculando a acurácia do modelo
acuracia = accuracy_score(y_test, y_pred)

# Exibindo o resultado
print(f'Acurácia do modelo: {acuracia:.2f}')
