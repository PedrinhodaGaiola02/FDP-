import matplotlib.pyplot as plt
import numpy as np
from math import pi

from functions import f, g, h, j
from tools import image, monte_carlo
from graphs import plot, scatter

dominio = np.linspace(0, 2*pi, 100)

imagem_f = image(f, dominio)
imagem_g = image(g, dominio)

dominio2 = np.linspace(f(0), g(0))

imagem_h = image(h, dominio2)
imagem_j = image(j, dominio2)

plot(dominio, imagem_f, imagem_g, dominio2, imagem_h, imagem_j)

area, pontos_dentro, pontos_fora = monte_carlo(f, g, h, j, number_of_points=100000)
scatter(pontos_dentro, pontos_fora)

print('Área estimada:', area)

plt.show()
