import matplotlib.pyplot as plt
import numpy as np
from math import pi

from functions import f, g
from tools import image, monte_carlo
from graphs import plot, scatter

dominio = np.linspace(0, 2*pi, 100)

imagem_f = image(f, dominio)
imagem_g = image(g, dominio)

plot(dominio, imagem_f, imagem_g)

area, pontos_dentro, pontos_fora = monte_carlo(f, g, dominio, number_of_points=100000)
scatter(pontos_dentro, pontos_fora)

print('Área estimada:', area)

plt.show()
