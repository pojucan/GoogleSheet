#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 10:38:01 2022

@author: pojucan
"""

import matplotlib.pyplot as plt
import pandas as pd

"""
Lendo um arquivo .txt com pandas no Google Sheets e criando um pandas data 
frame:
"""
# Database do Google Sheet:
pasta_id = '1tcWCH0K3ZeDecAI9JFrEOvimTEgMh5Na'

# Planilha 020 da pasta 020:
planilha_name = 'data'

url = f'https://docs.google.com/spreadsheets/d/1tcWCH0K3ZeDecAI9JFrEOvimTEgMh5Na/gviz/tq?tqx=out:csv&sheet={planilha_name}'

# Lendo os dados brutos:
df_brute = pd.read_csv(url)

# Mostrando na tela os valores:
print(df_brute)

# Tamanho da figura:
plt.figure(figsize=(8, 6))

# Range de plotagem:
plt.plot(df_brute['x'], df_brute['y'])

# plotagem do rótulo do eixo alterando tamanho da fonte e estilo:
plt.xlabel('Abscissas (u.c.)', fontsize = 12, fontweight = 'bold')

# Limita o intervalo da escala x (Dados de 1.0 à 12.0):
plt.xlim(0, 13)

# Passo de 1.0 na escala x dentro do range de 1.0 à 12.0:
plt.yticks(range(0, 12, 1))

# plotagem do rótulo do eixo alterando tamanho da fonte e estilo:
plt.ylabel('Ordenadas (u.c.)', fontsize = 12, fontweight = 'bold')

# Limita o intervalo da escala y (range da escala):
plt.ylim(0, 4096) 

# Passo de 1000.0 na escala y dentro do range de 2.0 à 4096.0:
plt.yticks(range(0, 4300, 300))

# Título do gráfico e propriedades:
plt.title('Gráfico X .vs. Y Exponencial', fontsize = 20)

# Exportação do gráfico para imagem:
plt.savefig('exponencial.png')

# Colocando a legenda no melhor lugar:
plt.legend(loc = 'best')

# Mostrando grade:
plt.grid()

# Mostrando o gráfico:
plt.show()

plt.close()