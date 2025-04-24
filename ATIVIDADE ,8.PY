

import pandas as pd
import matplotlib.pyplot as plt


# Base de dados simulada
dados = pd.DataFrame({
    'Setor': [
        'TI', 'RH', 'TI', 'Financeiro', 'RH', 'TI', 'Financeiro', 'Financeiro', 'RH', 'TI',
        'RH', 'Financeiro', 'TI', 'TI', 'RH', 'RH', 'TI', 'Financeiro', 'RH', 'TI',
        'TI', 'Financeiro', 'Financeiro', 'TI', 'RH', 'RH', 'TI', 'TI', 'Financeiro', 'RH'
    ],
    'Escolaridade': [
        'Superior', 'Médio', 'Superior', 'Superior', 'Médio', 'Pós', 'Superior', 'Pós', 'Médio', 'Superior',
        'Médio', 'Superior', 'Pós', 'Médio', 'Médio', 'Superior', 'Pós', 'Médio', 'Superior', 'Superior',
        'Médio', 'Pós', 'Médio', 'Pós', 'Médio', 'Superior', 'Pós', 'Superior', 'Superior', 'Médio'
    ],
    'Tempo_Deslocamento': [
        15, 20, 25, 10, 35, 50, 45, 30, 60, 90,
        15, 20, 22, 18, 80, 12, 16, 75, 28, 33,
        55, 60, 100, 120, 8, 7, 20, 18, 14, 11
    ]
})

# ---------------------
# Questão 1: Gráfico de barras - Distribuição por setor
plt.figure(figsize=(8, 5))
dados['Setor'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribuição de Funcionários por Setor')
plt.xlabel('Setor')
plt.ylabel('Quantidade')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# ---------------------
# Questão 2: Gráfico de setores (pizza) - Proporção de escolaridade
plt.figure(figsize=(6, 6))
dados['Escolaridade'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%',
    colors=['lightcoral', 'gold', 'lightgreen']
)
plt.title('Proporção de Escolaridade dos Funcionários')
plt.ylabel('')
plt.tight_layout()
plt.show()

# ---------------------
# Questão 3: Gráfico de boxplot - Tempo de deslocamento
plt.figure(figsize=(10, 6))
plt.boxplot(
    dados['Tempo_Deslocamento'],
    vert=False,
    patch_artist=True,
    boxprops=dict(facecolor='lightblue', color='blue'),
    medianprops=dict(color='red'),
    whiskerprops=dict(color='black'),
    capprops=dict(color='black'),
    flierprops=dict(marker='o', markerfacecolor='orange', markersize=8)
)
plt.title("Tempo de Deslocamento até o Trabalho (minutos)")
plt.xlabel("Minutos")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


#Qual setor possui mais funcionários?
# O setor de TI

#Existe algum setor com poucos colaboradores?
# O setor Financeiro

#Qual é o nível de escolaridade predominante?
# Nivel Superior

#Existe equilíbrio entre os grupos?
# Sim

#Qual é a mediana do tempo de deslocamento?
#  25 minutos

#Existem outliers?
# sim

#O tempo está concentrado em alguma faixa?
#  Entre 20 a 40 minutos