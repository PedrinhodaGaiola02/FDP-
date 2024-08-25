import numpy as np
import matplotlib.pyplot as plt

def gera_sequencia(n, a):
    sequencia = np.zeros(n)
    sequencia[0] = 0.1

    for i in range(n - 1):
        sequencia[i+1] = a*sequencia[i] * (1-sequencia[i])

    return sequencia

N = 5000
a = 1

sequencia = gera_sequencia(N, a)
x = np.arange(N)

plt.scatter(x, sequencia)
plt.show()
