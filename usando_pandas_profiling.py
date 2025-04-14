# Importação das bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport

# Caminho do arquivo
caminho_arquivo = "/home/oliveira/Downloads/Python Para Data Science/codigo/cap_07/placement.csv"

# Verificando se o arquivo existe antes de carregar
import os
if not os.path.exists(caminho_arquivo):
    print(f"❌ Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
else:
    # Corrigido para ler CSV corretamente
    df = pd.read_csv(caminho_arquivo, encoding="utf-8")

    # Criando o relatório
    arquivo = ProfileReport(df, explorative=True)
    arquivo.to_file(output_file="relatorio.html")

    print("✅ Relatório gerado com sucesso! Verifique o arquivo 'relatorio.html'.")
