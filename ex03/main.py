import numpy as np

def gera_sequencia(n, a):
    sequencia = np.zeros(n)
    sequencia[0] = 0.1

    for i in range(n - 1):
        sequencia[i+1] = a*sequencia[i] * (1-sequencia[i])

    return sequencia

sequencia = gera_sequencia(5000, 1)
media = np.mean(sequencia)
desvio_padrao = np.std(sequencia)

print('Media:', media)
print('Desvio padrão:', desvio_padrao)
