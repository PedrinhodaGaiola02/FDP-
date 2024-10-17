import matplotlib.pyplot as plt
from lib import calcula_pi
import pandas as pd

Ns = []
dxs = []
Fs = []
somas = []
xs = []
pis = []
erros = []

for N in range(10, 10000, 50):
    dx, x, F, soma, pi, erro = calcula_pi(N)
    Ns.append(N)
    dxs.append(dx)
    Fs.append(F)
    somas.append(soma)
    xs.append(x)
    pis.append(pi)
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
tabela = pd.DataFrame({
    'N': Ns,
    'Erro': erros,
})

print(tabela)
