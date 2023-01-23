import pandas as pd

# Carregando dados de exemplo
df = pd.read_csv("data.csv")

# Verificando as primeiras linhas dos dados
print(df.head())

# Verificando as informações do conjunto de dados
print(df.info())

# Verificando se existem valores ausentes
print(df.isnull().sum())

# Preenchendo valores ausentes com a média
df['coluna_com_valores_ausentes'] = df['coluna_com_valores_ausentes'].fillna(df['coluna_com_valores_ausentes'].mean())

# Verificando se ainda existem valores ausentes
print(df.isnull().sum())

# Salvando o conjunto de dados limpo em um arquivo CSV
df.to_csv("data_cleaned.csv", index=False)