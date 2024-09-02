import numpy as np

def multiplica(matrizA, matrizB):
    m = len(matrizA)
    r = len(matrizA[0])
    n = len(matrizB[0])

    if r != len(matrizB):
        raise ValueError("matrizes incompativeis")

    matrizResultado = np.zeros(shape =(m,n), dtype=np.float64)

    for i in range(m):
        for j in range(r):
            for k in range(n):
                matrizResultado[i,k] += matrizA[i,j]*matrizB[j,k]

    return matrizResultado
