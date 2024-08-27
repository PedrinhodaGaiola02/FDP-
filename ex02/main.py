##Exercício 2
import numpy as np
import time 
import matplotlib.pyplot as plt


def multiplica_lenta (A, B, m, n, r):
    C1 = np.zeros(shape =(m,n), dtype=np.float64)

    for i in range(m):
        for j in range(n):
            for k in range(r):
                C1[i,j] += A[i,k]*B[k,j]

    return C1

m = 2000
r = 2000
n = 2000

A = np.random.rand(m,r)
B = np.random.rand(r,n)

tinicial = time.time()
# C1 = multiplica_lenta(A, B, m, n, r)
tempo_corrido1 = time.time() - tinicial

print('Tempo corrido para calcular1 =', tempo_corrido1, '\n')

def multiplica_rapida (A, B, m, n, r):
    C2 = A@B
    return C2

tinicial = time.time()
C2 = multiplica_rapida(A, B, m, n, r)
tempo_corrido2 = time.time() - tinicial

print('Tempo corrido para calcular2 =', tempo_corrido2, '\n')




