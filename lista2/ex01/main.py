from matplotlib import pyplot as plt
from lib import jogar_dados

## apenas frufru
from progress.bar import Bar


numero_de_dados = 3
numero_de_iteracoes = 100000

somas = []

## apenas frufru
bar = Bar('Processing', max=numero_de_iteracoes)

for i in range(numero_de_iteracoes):
    dados = jogar_dados(numero_de_dados)
    somas.append(sum(dados))
    bar.next()

print("\nAbrindo gráfico")

plt.hist(somas, bins=range(numero_de_dados, 6 * numero_de_dados + 2), edgecolor='black')
plt.xticks(range(numero_de_dados, 6 * numero_de_dados + 1))
plt.show()
