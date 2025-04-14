# app.py
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.express as px

# Título
st.title("📘 Previsão de Notas com Regresão Linear")

# Dados simulados
dados = {
    'Horas_estudo': [1, 2, 3, 4, 5],
    'Nota': [35, 45, 50, 65, 70]
}
df = pd.DataFrame(dados)

# Treinar o modelo
X = df[['Horas_estudo']]
y = df['Nota']
modelo = LinearRegression()
modelo.fit(X, y)

# Interface - Slider para horas de estudo
horas = st.slider('Quantas horas você estudou?', 0.0, 10.0, 4.0, step=0.5)

# Previsão
previsao = modelo.predict([[horas]])[0]
st.write(f"📊 Para **{horas} horas** de estudo, a nota prevista é **{previsao:.2f}**.")

# Gráfico interativo
df['Previsao'] = modelo.predict(X)
fig = px.scatter(df, x='Horas_estudo', y='Nota', title='Regressão Linear - Notas x Horas de Estudo')
fig.add_scatter(x=df['Horas_estudo'], y=df['Previsao'], mode='lines', name='Linha de Regressão', line=dict(color='red'))

# Exibir o gráfico
st.plotly_chart(fig)
