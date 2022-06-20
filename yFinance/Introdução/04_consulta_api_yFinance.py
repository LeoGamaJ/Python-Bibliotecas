import yfinance as yf
yf.pdr_override()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import seaborn as sns

tickers = ["ABEV3.SA", "ITSA4.SA", "WEGE3.SA", "USIM5.SA", "VALE3.SA"]

carteira = web.get_data_yahoo(tickers, period="5y")["Adj Close"]
ibov = web.get_data_yahoo("^BVSP", period="5y")["Adj Close"]

print(carteira)

print(ibov)

sns.set()   # Inicializando o Seaborn
carteira.plot(figsize=(22,8))

# Normalizando carteira
carteira_normalizada = (carteira / carteira.iloc[0])
print(carteira)

# Plotando gráfico de carteira normalizada
carteira_normalizada.plot(figsize=(18,8))

# Normalizando saldo
carteira_normalizada["Saldo"] = carteira_normalizada.sum(axis=1)
print(carteira_normalizada)

ibov_normalizado = (ibov / ibov.iloc[0])
print(ibov_normalizado)

carteira_normalizada["Saldo"].plot(figsize=(18,8), label="Minha Carteira")
ibov_normalizado.plot(label="IBOV")
plt.legend()

