from math import sqrt
import matplotlib.pyplot as plt

def phi(x):
    phi = 1/sqrt(x)
    return phi 

x_velho = 0.75


iteracoes = 100
eixo_x = [0.75, ]
eixo_y = [1.1547005383792517, ]

for i in range(iteracoes):
    x_novo = phi(x_velho)
    eixo_y.append(phi(x_velho))
    x_velho = x_novo
    eixo_x.append(x_novo)
    print('Valor de X:', x_novo, 'Eixo X:', eixo_x)

plt.plot(eixo_x, eixo_y)
plt.show()
