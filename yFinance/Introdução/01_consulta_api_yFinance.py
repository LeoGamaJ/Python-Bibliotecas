import sys
import yfinance as yf
from matplotlib import pyplot as plt 
#%matplotlib inline

# Ação da consulta armazenada numa variável
lmt = yf.Ticker("LMT")

# Exibindo Informações
print(lmt.info)
# Exibindo Histórico
hist = lmt.history(period="max")
print(hist)

# Gráfico de fechamento da ação
plt.plot(hist["Close"], label="LMT")
plt.xlabel("Data")
plt.ylabel("Cotação de Fechamento (USD)")

plt.legend()
plt.show()

# Agrupando dividendos
dividendos = hist["Dividends"].resample("Y").sum()
print(dividendos)

# Gráfico dos dividendos agrupados
plt.plot(dividendos.index.year[:-2], dividendos[:-2], label="LMT")
plt.xlabel("Data")
plt.ylabel("Dividendos Anuais (USD)")
plt.legend()
plt.show()