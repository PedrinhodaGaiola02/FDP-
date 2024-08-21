##Exercício 2
import numpy as np
import time 

tinicial = time.time()

def multiplica_lenta (A, B, m, n, r):
    C1 = np.zeros(shape =(m,n), dtype=np.float64)

    for i in range(m):
        for j in range(n):
            for k in range(r):
                C1[i,j] += A[i,k]*B[k,j]

    return C1

m = 10
r = 14
n = 20

A = np.random.rand(m,r)
B = np.random.rand(r,n)
I = np.identity(m)
C1 = multiplica_lenta(A, B, m, n, r)


print('Matriz C1=', C1)

print('Tempo corrido para calcular =', time.time() - tinicial)

def multiplica_rapida (A, B, m, n, r):
    C2 = A@B
    return C2
C2 = multiplica_rapida(A, B, m, n, r)
print('Matriz C2 = ', C2)






