import numpy as np
from matplotlib import pyplot as plt
from lib import calcula_pi, escreve
import math

iteracoes = (
    1000,
    10000,
    100000,

)
estimativas = 4

pis = np.zeros(shape=(estimativas, len(iteracoes)))
medias = np.zeros(shape=(len(iteracoes)))

for j, iteracao in enumerate(iteracoes):
    for i in range(estimativas):
        pis[i][j] = calcula_pi(iteracoes[j], 'Estimativa {} X {}'.format(i + 1, iteracoes[j]))
        medias[j] = sum(pis[:, j]) / estimativas
        escreve(pis, medias)

erros = tuple(map(lambda x: abs(x - math.pi), medias))

plt.loglog(iteracoes, erros)
plt.show()
