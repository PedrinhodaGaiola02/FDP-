import numpy as np
from domain import r
from progress.bar import Bar

N = 10000
M = 1000

distancias = []

bar = Bar("Caminhando...", max=M)
for i in range(M):
    viagem = r(10000)
    distancia_quadratica_percorrida = np.sum(viagem[-1] ** 2)
    distancias.append(distancia_quadratica_percorrida)
    bar.next()
bar.finish()

media = (1/M) * sum(distancias)
print("Media:", media)
