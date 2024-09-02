##Exercício 2
import numpy as np
import time
import matplotlib.pyplot as plt
from lenta import multiplica as multiplica_lenta
from rapida import multiplica as multiplica_rapida

def mede_tempo(multiplica):
    tempo_inicial = time.time()

    matrizA = np.random.rand(dimensao, dimensao)
    matrizB = np.random.rand(dimensao, dimensao)

    matrizC = multiplica(matrizA, matrizB)
    print('{} OK'.format(dimensao))

    tempo_final = time.time()
    tempo_percorrido = tempo_final - tempo_inicial

    return tempo_percorrido

dimensoes = [100, 250, 500, 700, 1000]
tempos_lenta = []
tempos_rapida = []

for dimensao in dimensoes:
    tempo_lenta_percorrido = mede_tempo(multiplica_lenta)
    tempo_rapida_percorrido = mede_tempo(multiplica_rapida)
    tempos_lenta.append(tempo_lenta_percorrido)
    tempos_rapida.append(tempo_rapida_percorrido)

plt.loglog(dimensoes, tempos_lenta, '-r')
plt.loglog(dimensoes, tempos_rapida, '-g')
plt.xlabel('dimensao')
plt.ylabel('tempos [s]')
plt.title('Grafico dimensao X tempo')
plt.legend(['Lenta', 'Rapida'])
plt.grid()
plt.show()

