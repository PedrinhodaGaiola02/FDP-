import math 
import numpy as np
import matplotlib.pyplot as plt
from lib import calcula_pi
import pandas as pd


Ns = []
Δxs = []
Fs = []
Soma_de_Riemanns = []
xs = []
πs = []
erros = []

for N in range(10, 10000, 50):
    Δx, x, F, Soma_de_Riemann, π, erro = calcula_pi(N)
    Ns.append(N)
    Δxs.append(Δx)
    Fs.append(F)
    Soma_de_Riemanns.append(Soma_de_Riemann)
    xs.append(x)
    πs.append(π)
    erros.append(erro)



#Gráfico plotado
plt.figure(figsize=(10, 6))
plt.plot(Ns, erros, marker='o', linestyle='-', color='b', label='Erro')
plt.title('Erro na Aproximação de π em Função de N')
plt.xlabel('N')
plt.ylabel('Erro (|π - π_aproximado|)')
plt.grid(True)
plt.legend()
plt.show()

#Tabela dos resultados
Tabela = pd.DataFrame({
    'N': Ns,
    'Erro': erros,
})

print(Tabela)