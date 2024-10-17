import numpy as np
from math import pi
from pandas import DataFrame

from functions import f, g, h, j
from tools import image, monte_carlo

N = [
    ("10^3", 1000),
    ("10^4", 10000),
    ("10^5", 100000),
    ("10^6", 1000000),
    # ("10^7", 10000000),
]

dominio = np.linspace(0, 2*pi, 100)

imagem_f = image(f, dominio)
imagem_g = image(g, dominio)

dominio2 = np.linspace(f(0), g(0))

imagem_h = image(h, dominio2)
imagem_j = image(j, dominio2)

areas = []

for (key, number_of_points) in N:
    area, pontos_dentro, pontos_fora = monte_carlo(f, g, h, j, number_of_points, label="Processando com N = {}".format(key))
    areas.append(area)

tabela = DataFrame({
    'N': np.array(N)[:,0],
    'Área estimada': areas,
})

print(tabela)
