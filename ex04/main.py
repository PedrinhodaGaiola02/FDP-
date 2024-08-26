import numpy as np
import matplotlib.pyplot as plt

def gera_sequencia(n, a):
    sequencia = np.zeros(n)
    sequencia[0] = 0.1

    for i in range(n - 1):
        sequencia[i+1] = a*sequencia[i] * (1-sequencia[i])

    return sequencia

N = 50
x = np.arange(N)

seq1 = gera_sequencia(N, 1)
seq2 = gera_sequencia(N, 1.5)
seq3 = gera_sequencia(N, 2)
seq4 = gera_sequencia(N, 3)
seq5 = gera_sequencia(N, 3.8)
seq6 = gera_sequencia(N, 4)

plt.scatter(x, seq1, s=0.1, c="black")
plt.plot(x, seq1, c="black")

plt.scatter(x, seq2, s=0.1, c="blue")
plt.plot(x, seq2, c="blue")

plt.scatter(x, seq3, s=0.1, c="red")
plt.plot(x, seq3, c="red")

plt.scatter(x, seq4, s=0.1, c="purple")
plt.plot(x, seq4, c="purple")

plt.scatter(x, seq5, s=0.1, c="green")
plt.plot(x, seq5, c="green")

plt.scatter(x, seq6, s=0.1, c="orange")
plt.plot(x, seq6, c="orange")

plt.show()
