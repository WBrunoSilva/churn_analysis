#%%
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
#%%
# Importando os dados CSV para um DataFrame
df = pd.read_csv("../data/raw/telco-customer-churn.csv")

# Visualizando as primeiras linhas do DataFrame
df.head()

# Mostrando informações (Tipo de dados é Colunas)
df.info()

# Estatísticas descritivas das colunas numéricas e categóricas (objetos/strings)
df.describe()

# Estatística descritiva para colunas categóricas
df.describe(include='object')

# Contando valores nulos nas colunas
df.isnull().sum()

# Contagem de valores na coluna Churn
df["Churn"].value_counts()

# Contagem por proporção na coluna Churn
df["Churn"].value_counts(normalize=True)

# Visualizando a distribuição da variável alvo "Churn"
sns.countplot(x="Churn", data=df)
plt.title("Distribution of Churn")
plt.show()

# Listando valores únicos na coluna TotalCharges
df["TotalCharges"].unique()

# Convertendo a coluna para numérica e contando valores nulos
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors='coerce')
df["TotalCharges"].isnull().sum()

