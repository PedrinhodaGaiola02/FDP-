import numpy as np
import matplotlib.pyplot as plt
import utils
import time

dimensoes = range(0, 10000000, 1000000)
tempos = np.zeros(len(dimensoes))

for (i, dim) in enumerate(dimensoes):

    vetorA = np.random.randint(0, 10, size=dim)
    vetorB = np.random.randint(0, 10, size=dim)
    vetorC = np.zeros(dim)

    escalarAlpha = np.random.randint(0, 10)
    escalarBeta = np.random.randint(0, 10)

    tempo_i = time.time()
    vetorC = utils.combinacao_linear(escalarAlpha, vetorA, escalarBeta, vetorB)
    tempo_f = time.time()
    tempos[i] = tempo_f - tempo_i

plt.title("Combinacoes lineares")
plt.plot(dimensoes, tempos)
plt.loglog(dimensoes, tempos)
plt.show()

matrizA = np.random.rand(10, 10)
expoentes = range(2, 4)
tempos2 = np.zeros(len(expoentes))

for (i, exp) in enumerate(expoentes):
    tempo_i = time.time()
    utils.potencia(matrizA, exp)
    tempo_f = time.time()
    tempos2[i] = tempo_f - tempo_i

plt.title("Potencias")
plt.plot(expoentes, tempos2)
plt.loglog(dimensoes, tempos)
plt.show()

dimensoes2 = [500, 1000, 1500, 2000]
tempos3 = np.zeros(len(dimensoes2))

for (i, dim) in enumerate(dimensoes2):
    matrizA2 = np.random.rand(dim, dim)
    tempo_i = time.time()
    utils.potencia(matrizA2, 2)
    tempo_f = time.time()
    tempos3[i] = tempo_f - tempo_i

plt.title("Potencias 2")
# plt.plot(dimensoes2, tempos3)
plt.loglog(dimensoes2, tempos3)
plt.show()
