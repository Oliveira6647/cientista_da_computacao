import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Configura estilo dos gráficos
sns.set(style="whitegrid")

# Carregando o dataset
df = pd.read_csv('/home/oliveira/Downloads/Python Para Data Science/codigo/cap_13/diabetes_preprocessado.csv',
                 names=['#Gravidezes', 'Glicose', 'PD', 'DobraTriceps', 'Insulina', 'IMC', 'DPF', 'Idade', 'Classe'])

# Separação por classe
com_diabetes = df[df.Classe == 1]
sem_diabetes = df[df.Classe == 0]

# Loop pelas variáveis (colunas)
for variavel in df.columns:
    if variavel != 'Classe':
        # Criar figura com 3 subplots
        fig, axs = plt.subplots(1, 3, figsize=(18, 4))

        # 1. Histograma da variável na amostra total
        sns.histplot(df[variavel], kde=False, ax=axs[0], color="gray")
        axs[0].set_title(f'Histograma - {variavel} (Toda a amostra)')
        axs[0].set_xlabel(variavel)
        axs[0].set_ylabel("Frequência")

        # 2. Histogramas separados por classe
        sns.histplot(sem_diabetes[variavel], kde=False, color="blue", label="Sem Diabetes", ax=axs[1], alpha=0.6)
        sns.histplot(com_diabetes[variavel], kde=False, color="red", label="Com Diabetes", ax=axs[1], alpha=0.6)
        axs[1].set_title(f'Histograma - {variavel} por Classe')
        axs[1].legend()
        axs[1].set_xlabel(variavel)
        axs[1].set_ylabel("Frequência")

        # 3. Boxplot por classe
        sns.boxplot(x='Classe', y=variavel, data=df, ax=axs[2], palette="Set2")
        axs[2].set_title(f'Boxplot - {variavel} por Classe')
        axs[2].set_xlabel("Classe (0 = Sem Diabetes / 1 = Com Diabetes)")
        axs[2].set_ylabel(variavel)

        # Layout final
        plt.tight_layout()
        plt.show()
        plt.close(fig)  # Fecha a figura para evitar excesso de memória
