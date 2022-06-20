import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import seaborn as sns

# Definido variável e a relacionando ao dolar

tickers = ["^BVSP", "USDBRL=X"]
carteira = web.get_data_yahoo(tickers)["Close"]
print(carteira)

# Plotando Gráfico
sns.set()   # Inserindo recurso gráfico Seaborn
carteira.plot(subplots=True, figsize=(22,8))

# Removendo dados nulos
carteira = carteira.dropna()
print(carteira)

# Renomeando Colunas 
carteira.columns = ["DOLAR", "IBOV"]
print(carteira)

# Correlação entre variáveis
carteira.corr()

# Melhorando qualidade gráfica da correlação
sns.heatmap(carteira.corr(), annot=True)

carteira["DOLAR"].rolling(252).corr(carteira["IBOV"])

carteira["DOLAR"].rolling(252).corr(carteira["IBOV"]).plot(figsize=22,8))

# Ibov em dolares
carteira["INOV_DOLARIZADO"] = (carteira["IBOV"] / carteira["DOLAR"])
print(carteira)

