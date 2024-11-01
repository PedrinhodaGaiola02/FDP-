import numpy as np

## apenas frufru
from progress.bar import Bar

def calcula_pi(iteracoes, label):
    bar = Bar(label, max=iteracoes)
    dentro = 0

    for i in range(iteracoes):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)

        if (x**2 + y**2 < 1.0):
            dentro += 1

        bar.next()
    print()
    return 4 * dentro / iteracoes

def escreve(pis, medias):
    file = open("out.txt", "w")

    print("", file=file)
    print("        {:>13}   {:>13}   {:>13}   {:>13}   {:>13}".format("----------", "----------", "----------", "----------", "----------"), file=file)
    print("        {:>13}   {:>13}   {:>13}   {:>13}   {:>13}".format("N = 10^3", "N = 10^4", "N = 10^5", "N = 10^6", "N = 10^7"), file=file)
    print("        {:>13}   {:>13}   {:>13}   {:>13}   {:>13}".format("----------", "----------", "----------", "----------", "----------"), file=file)

    for i in range(len(pis)):
        print("{:>13,.4f}   {:>13,.4f}   {:>13,.4f}   {:>13,.4f}   {:>13,.4f}".format(*pis[i]), file=file)

    print("", file=file)
    print("", file=file)
    print("--------{:>13}   {:>13}   {:>13}   {:>13}   {:>13}".format("----------", "----------", "----------", "----------", "----------"), file=file)
    print("Média:  {:>13,.4f}   {:>13,.4f}   {:>13,.4f}   {:>13,.4f}   {:>13,.4f}".format(*medias), file=file)
    print("--------{:>13}   {:>13}   {:>13}   {:>13}   {:>13}".format("----------", "----------", "----------", "----------", "----------"), file=file)
