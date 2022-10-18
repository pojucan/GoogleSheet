A matriz dos dados Raman ($R_{m \times n}$) onde $m=1024$ e $n=2$, podendo ser escrita da seguinte forma:

$$\begin{equation}

R_{m \times n} = \begin{bmatrix}
r_{1,1} & r_{1,2} \\ 
r_{2,1} & r_{2,2} \\ 
r_{3,1} & r_{3,2} \\ 
.       & .     \\ 
.       & .     \\ 
.       & .     \\ 
r_{1024,1} & r_{1024,2} \\ 
\end{bmatrix}
\end{equation}$$

Onde $r_{m,1} = [d_{1}, d_{2}, d_{3}, . . ., d_{m}]$ é chamado de Deslocamento Raman e $r_{m,2} = [i_{1}, i_{2}, i_{3}, ..., i_{m}]$, de Intensidade. Sendo assim, tem-se:

$$\begin{equation}
R_{1024 \times 2} = \begin{bmatrix}
 d_{1} & i_{1}        \\
 d_{2} & i_{2}        \\
 d_{3} & i_{3}        \\
 .      & .            \\
 .      & .               \\
 .      & .               \\
 d_{1024} & i_{1024}  \\
\end{bmatrix}
\end{equation}$$

Tais valores compõe cada uma das planilhas do Google Sheets a serem lidas pelo script $\textit{\color{red}{<exponencial.py>}}$ de forma que cada planilha é um arquivo, ou seja, uma análise de espectroscopia Raman.

Cada amostra foi analisada em 20 (vinte) campos diferentes. Cada gráfico de amostra apresentado, trata-se da média de cada campo de análise, de forma que:


