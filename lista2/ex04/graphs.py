from matplotlib import pyplot as plt
from math import pi

def plot(domain, image_f, image_g):
    plt.plot(domain, image_f, 'r')
    plt.plot(domain, image_g, 'g')

    plt.xlabel('x')
    plt.ylabel('y')

    plt.legend([
        '$f(x) = 1 + \\frac{1}{2}sin^{3}(2x)$',
        '$g(x) = 3 + \\frac{1}{2}cos^{5}(3x)$'
    ])

    plt.xticks([0, 2*pi], labels=["0", "2π"])

def scatter(pontos_dentro, pontos_fora):
    plt.scatter(pontos_dentro[:,0], pontos_dentro[:, 1], s=0.05, c="blue")
    plt.scatter(pontos_fora[:,0], pontos_fora[:, 1], s=0.05, c="gray")

