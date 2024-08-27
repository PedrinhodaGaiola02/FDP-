import numpy as np

def sequencia(n, a):
    sequencia = np.zeros(n)
    sequencia[0] = 0.1

    for i in range(n - 1):
        sequencia[i+1] = a*sequencia[i] * (1-sequencia[i])

    return sequencia