##Exercício 2
import numpy as np
import time 
import matplotlib.pyplot as plt

dimens = [50, 100, 150, 200]
#dimr = [50, 100, 150, 200]
#dimn = [50, 100, 150, 200]
tempos1 = []
tempos2 = []
for i in range (len(dimens)):
    n = dimens[i]
    A = np.random.rand(n,n)
    B = np.random.rand(n,n)

    def multiplica_lenta (A, B, n):
        C1 = np.zeros(shape =(n,n), dtype=np.float64)
        for i in range(n):
            C1[i,i] += A[i,i]*B[i,i]
        return C1

    tinicial = time.time()
    C1 = multiplica_lenta(A, B, n)
    tempo_corrido1 = time.time() - tinicial

    #print('Tempo corrido para calcular1 =', tempo_corrido1, '\n')

    def multiplica_rapida (A, B, n):
        C2 = A@B
        return C2

    tinicial = time.time()
    C2 = multiplica_rapida(A, B, n)
    tempo_corrido2 = time.time() - tinicial

    #print('Tempo corrido para calcular2 =', tempo_corrido2, '\n')
    tempos1.append(tempo_corrido1)
    print('Tabela de tempos da multilenta e', i, n, tempos1[i], '\n')
    tempos2.append(tempo_corrido2)
    print('Tabela de tempos da multirapida e', i, n, tempos2[i], '\n')



