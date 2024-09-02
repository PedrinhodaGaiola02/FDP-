##Exercício 2
import numpy as np
import time
import matplotlib.pyplot as plt
from lenta import multiplica

dimensoes = [100, 150, 200, 250, 300]
tempos = []

for dimensao in dimensoes:
    tempo_inicial = time.time()

    matrizA = np.random.rand(dimensao, dimensao)
    matrizB = np.random.rand(dimensao, dimensao)

    matrizC = multiplica(matrizA, matrizB)
    print('{} OK'.format(dimensao))

    tempo_final = time.time()
    tempo_percorrido = tempo_final - tempo_inicial
    tempos.append(tempo_percorrido)

plt.loglog(dimensoes, tempos, '-r')
plt.xlabel('dimensao')
plt.ylabel('tempos [s]')
plt.title('Grafico dimensao X tempo')
plt.grid()
plt.show()

