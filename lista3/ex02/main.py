import matplotlib.pyplot as plt
import numpy as np

def phi(x):
    phi = 1/np.sqrt(x)
    return phi 

x_velho = 0.75


iteracoes = 2
valores_de_x = [x_velho]
valores_da_funcao = []

for i in range(iteracoes):
    x_novo = phi(x_velho)
    valores_da_funcao.append(phi(x_velho))
    valores_de_x.append(x_novo)
    x_velho = x_novo
    print('Valor de X:', valores_de_x)
    print('Valor de da funcao:', valores_da_funcao)

def y(x):
    return x

eixo_x = np.linspace(0, 1.5)

plt.plot(eixo_x, phi(eixo_x))
plt.plot(eixo_x, y(eixo_x), linestyle='--')
plt.show()
