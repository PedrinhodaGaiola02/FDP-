import numpy as np
import matplotlib.pyplot as plt
from gerador import sequencia

N = 1000
A = 300

coeficientes = np.linspace(0, 4, A)
sequencias = np.zeros((A, N))

for i, a in enumerate(coeficientes):
    sequencias[i] = sequencia(N, a)

for n in range(N):
    sequenciaEstudada = np.zeros(A)

    for (i, seq) in enumerate(sequencias):
        sequenciaEstudada[i] = seq[n]

    plt.scatter(coeficientes, sequenciaEstudada, s=0.1, c="black")

plt.show()
