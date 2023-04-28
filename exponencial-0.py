#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 10:38:01 2022

@author: pojucan
"""

import matplotlib.pyplot as plt
import pandas as pd

"""
Lendo um arquivo .xlsx do Google Sheets com pandas e abordando por data frame:
"""
# ID do arquivo no Google Sheets::
pasta_id = '1tcWCH0K3ZeDecAI9JFrEOvimTEgMh5Na'

# Planilha data da pasta data no Google Sheets:
planilha_name = 'data'

url = f'https://docs.google.com/spreadsheets/d/1tcWCH0K3ZeDecAI9JFrEOvimTEgMh5Na/gviz/tq?tqx=out:csv&sheet={planilha_name}'

# Lendo os dados brutos no Google Sheets:
df_brute = pd.read_csv(url)

# Mostrando na tela os valores de dados brutos:
print(df_brute)

# Configura o tamanho da figura:
plt.figure(figsize=(8, 6))

# Plotagem do gráfico via data frame:
plt.plot(df_brute['x'], df_brute['y'])

# Escrita do rótulo no eixo X alterando tamanho da fonte e estilo:
plt.xlabel('Abscissas (u.c.)', fontsize = 12, fontweight = 'bold')

# Limita o intervalo da escala no eixo X (Dados de 1.0 à 12.0):
plt.xlim(0, 13)

# Passo de 1.0 na escala do eixo X dentro do range de 1.0 à 12.0:
plt.yticks(range(0, 12, 1))

# Escrita do rótulo no eixo Y alterando tamanho da fonte e estilo:
plt.ylabel('Ordenadas (u.c.)', fontsize = 12, fontweight = 'bold')

# Limita o intervalo da escala no eixo Y (range da escala):
plt.ylim(0, 4096) 

# Passo de 1000.0 na escala do eixo Y dentro do range de 2.0 à 4096.0:
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