import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

import yfinance as yf

yf.pdr_override()

#
ibov = web.get_data_yahoo("^BVSP")
ibov.head()
ibov.tail()

#
ibov["Close"].plot(figsize=(22,8), label="IBOV")
ibov["Close"].rolling(21).mean().plot(label="MM21")  # média móvel de 21 dias
ibov["Close"].rolling(200).mean().plot(label="MM200")  # média móvel de 200 dias
plt.legend()

#
ibov_fatiado = ibov[ibov.index.year == 2022]

ibov_fatiado["Close"].plot(figsize=(22,8), label="IBOV_Fatiado")
ibov_fatiado["Close"].rolling(21).mean().plot(label="MM21_fat")  # média móvel de 21 dias
ibov_fatiado["Close"].rolling(200).mean().plot(label="MM200_fat")  # média móvel de 200 dias
plt.legend()

#
ibov_fatiado2 = ibov[(ibov.index.year >= 2018) & (ibov.index.year <= 2021)]

ibov_fatiado2["Close"].plot(figsize=(22,8), label="IBOV_Fat2")
ibov_fatiado2["Close"].rolling(21).mean().plot(label="MM21_fat2")  # média móvel de 21 dias
ibov_fatiado2["Close"].rolling(200).mean().plot(label="MM200_fat2")  # média móvel de 200 dias
plt.legend()