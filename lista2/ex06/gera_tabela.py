import numpy as np
from pandas import DataFrame
from utils import monte_carlo

N = [
    ("10^3", 1000),
    ("10^4", 10000),
    ("10^5", 100000),
    ("10^6", 1000000),
    ("10^7", 10000000),
    #("10^8", 100000000),
]

valores_de_pi = []

for key, numero_de_pontos in N:
    volume, dentro, fora = monte_carlo(numero_de_pontos, label="Processando com N = {}".format(key))
    valores_de_pi.append(volume * (3/4))

N = np.array(N)
valores_de_pi = np.array(valores_de_pi)

volumes = DataFrame({
    'N': N[:, 0],
    'V': valores_de_pi,
    'Erro': abs(valores_de_pi - np.pi)
})

print(volumes)
