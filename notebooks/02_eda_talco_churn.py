# Importando bibliotecas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando dados 
df = pd.read_csv("../data/raw/telco-customer-churn.csv")
df.head()

# Verificando clientes com tempo de contrado "Tenure" igual a 0
df[['customerID','tenure','TotalCharges']].loc[df['tenure']==0]

# Cálculo da proporção de Churn para cada tipo de contrato 
df.groupby('Contract')['Churn'].value_counts(normalize=True)

#Visualização gráfica da taxa de Chrun por tipo de contrato
churn_rate = df.groupby('Contract')['Churn'].apply(lambda x: (x=='Yes').mean()).reset_index()
sns.barplot(x='Contract', y='Churn', data=churn_rate)
plt.title('Churn Rate by Contract Type')
plt.ylabel('Churn Rate')
plt.xlabel('Contract Type')
plt.show()

# Proporção de Churn por tipo de serviço de internet
df.groupby('InternetService')['Churn'].value_counts(normalize=True)

# Vizualiçaão gráfica taxa de Churn por tipos de "InternetService"
churn_rate_internet = df.groupby('InternetService')['Churn'].apply(lambda x:(x=='Yes').mean()).reset_index()
sns.barplot(x='InternetService', y='Churn', data=churn_rate_internet)
plt.title('Churn rate by Internet Service Type')
plt.ylabel('Churn Rate')
plt.xlabel('Internet Service Type')
plt.show()


# Cruzando as tabelas para ver a relação entre tipo de contrato e serviço de internet
pd.crosstab(df['Contract'], df['InternetService'],normalize='index')

# Cruzando as tabelas e verificando o Churn
pd.crosstab([df['Contract'], df['InternetService']],df['Churn'], normalize='index')


# Analisando impacto do "TechSupport" no Churn
df.groupby('TechSupport')['Churn'].value_counts(normalize=True)

# Visualização gráfica da Taxa de Churn para quem não possui "TechSupport"
churn_rate_techsupport = df.groupby('TechSupport')['Churn'].apply(lambda x: (x=='Yes').mean()).reset_index()
sns.barplot(x='TechSupport',y='Churn',data=churn_rate_techsupport)
plt.title('Churn rate by Tech Support')
plt.ylabel('Churn Rate')
plt.xlabel('Tech Support')
plt.show()

# Analisando impacto do "OnlineSecurity" no Churn
df.groupby('OnlineSecurity')['Churn'].value_counts(normalize=True)

# Visualização gráfica da taxa de Chrun para que não possui "OnlineSecurity"
churn_rate_onlinesecurity = df.groupby('OnlineSecurity')['Churn'].apply(lambda x: (x=='Yes').mean()).reset_index()
sns.barplot(x='OnlineSecurity', y='Churn', data=churn_rate_onlinesecurity)
plt.title('Churn rate by Online Security')
plt.ylabel('Churn Rate')
plt.xlabel('Online Security')
plt.show()


# Cruzando tabelas para verificar a relação entre "Contract","TechSupport" e "Churn"
pd.crosstab([df['Contract'],df['TechSupport']],df['Churn'],normalize='index')

# Cruzando tabelas para verificar a relação entre "Contract", "OnlineSecurity" e "Churn"
pd.crosstab([df['Contract'],df['OnlineSecurity']],df['Churn'],normalize='index')

