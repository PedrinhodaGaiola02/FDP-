##Exercício 2
import numpy as np
import time 

def multiplica_lenta (A, B, m, n, r):
    C = np.zeros(shape =(m,n), dtype=np.float64)

    for i in range(m):
        for j in range(n):
            for k in range(r):
                C[i,j] += A[i,k]*B[k,j]

    return C

m = 4
r = 4 
n = 4

A = np.random.rand(m,r)
B = np.random.rand(r,n)
I = np.identity(m)
C = multiplica_lenta(A, I, m, n, r)

print('Matriz A=', A)

print('Matriz C=', C)







