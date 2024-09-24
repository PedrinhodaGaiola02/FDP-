import numpy as np
import utils
import time

## Medir tempo inicial
tempo_inicial = time.time()

N = 3

# O computador precisa saber quais serao os vetores
vetorA = np.random.randint(0, 10, size=N)
vetorB = np.random.randint(0, 10, size=N)
vetorC = np.zeros(N)

print("Vetores gerados:")
print("Vetor A:", vetorA)
print("Vetor B:", vetorB)

# O computador precisa saber quais serao os escalares
escalarAlpha = np.random.randint(0, 10)
escalarBeta = np.random.randint(0, 10)

print("Escalares gerados:")
print("Escalar Alpha:", escalarAlpha)
print("Escalar Beta:", escalarBeta)

# O computador precisa saber o que fazer com tais vetores
vetorC = utils.combinacao_linear(escalarAlpha, vetorA, escalarBeta, vetorB)

print("Resultado:", vetorC)

# Medir tempo final
tempo_final = time.time()

# Calcular diferença e mostrar na tela
variacao_de_tempo = tempo_final - tempo_inicial
print("Tempo gasto: {}s".format(variacao_de_tempo))
