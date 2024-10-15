import math
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

valores_de_x= np.linspace(0, 2 * math.pi, 100)

F = []
G = []

for x in valores_de_x:
    F_x = 1 + 1/2 * (math.sin(2 * x))**3
    G_x = 3 + 1/2 * (math.cos(3 * x))**5
    F.append(F_x)
    G.append(G_x)

plt.plot(valores_de_x, F, 'o-r')
plt.plot(valores_de_x, G, 'o-g')
plt.xlabel('Valores de X em Radianos')
plt.ylabel('Valores de F(x) e G(x)')
plt.legend(['F(x)', 'G(x)'])
plt.title('Funções seno e cosseno em função de x no intervalo [0, 2π]')
plt.show()

#Definindo a variável símbolica
x = sp.symbols('x')


#definindo as funções
f =  1 + (1/2) * sp.sin(2 * x)**3
g = 3 + (1/2) * sp.cos(3 * x)**5


#Encontrando os pontos de intersecção
interseccoes = sp.solve(sp.Eq(f, g), x)


#Calculando a área entre as curvas

area = sp.integrate(sp.Abs(f - g), (x, 0, 2 * sp.pi))

print('Aréa entre as curvas = ', area)