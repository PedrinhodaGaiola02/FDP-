from math import sqrt
import matplotlib.pyplot as plt
import numpy as np


def phi(x):
    phi = 1/sqrt(x)
    return phi 

x_velho = 0.75


iteracoes = 100
valores_de_x = [0.75, ]
valores_de_phi = [1.1547005383792517, ]

for i in range(iteracoes):
    x_novo = phi(x_velho)
    valores_de_phi.append(phi(x_velho))
    x_velho = x_novo
    valores_de_x.append(x_novo)
    #print('Valor de X:', valores_de_x)


def y(x):
    y = x
    return y


m = np.linspace(0, 1.5)
print(m)


