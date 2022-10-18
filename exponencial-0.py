#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 10:38:01 2022

@author: pojucan
"""

import matplotlib.pyplot as plt
import pandas as pd

"""
Lendo um arquivo .xlsx com pandas do Google Sheets e abordando por data 
frame:
"""
# Database do Google Sheet:
pasta_id = '1tcWCH0K3ZeDecAI9JFrEOvimTEgMh5Na'

# Planilha 020 da pasta 020:
planilha_name = 'data'

url = f'https://docs.google.com/spreadsheets/d/1tcWCH0K3ZeDecAI9JFrEOvimTEgMh5Na/gviz/tq?tqx=out:csv&sheet={planilha_name}'

# Lendo os dados brutos:
df_brute = pd.read_csv(url)

# Mostrando na tela os valores de dados brutos:
print(df_brute)

# Configura o tamanho da figura:
plt.figure(figsize=(8, 6))

# Plotagem do gráfico via data frame:
plt.plot(df_brute['x'], df_brute['y'])

# Escrita do rótulo do eixo X alterando tamanho da fonte e estilo:
plt.xlabel('Abscissas (u.c.)', fontsize = 12, fontweight = 'bold')

# Limita o intervalo da escala X (Dados de 1.0 à 12.0):
plt.xlim(0, 13)

# Passo de 1.0 na escala X dentro do range de 1.0 à 12.0:
plt.yticks(range(0, 12, 1))

# Escrita do rótulo do eixo Y alterando tamanho da fonte e estilo:
plt.ylabel('Ordenadas (u.c.)', fontsize = 12, fontweight = 'bold')

# Limita o intervalo da escala Y (range da escala):
plt.ylim(0, 4096) 

# Passo de 1000.0 na escala Y dentro do range de 2.0 à 4096.0:
plt.yticks(range(0, 4300, 300))

# Título do gráfico e tamanho da fonte:
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