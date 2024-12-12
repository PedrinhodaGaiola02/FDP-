from matplotlib import image
from matplotlib import pyplot as plt
import numpy as np

img = image.imread(r"D:\Documents\GitHub\FDP-\lista4\processamento_imagens\ex02\stinkbug.png")

print(img.shape)
print(img)

def build_circulo(x, y, raio):
    circulo = []

    for i in range(x - raio, x + raio):
        for j in range(y - raio, y + raio):
            if (i - x)**2 + (j - y)**2 <= raio**2:
                circulo.append((i, j))

    return circulo

def desenha_circulo(img, circulo, cor):
    for (x, y) in circulo:
        if (x < img.shape[0] and x >= 0 and y < img.shape[1] and y >= 0):
            img[x, y] = cor

    return img

def listras(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                if j % 15 == 0 or i % 15 == 0:
                    img[i, j, k] = 255

    return img

img = listras(img)

num_bolas = 10
raio = 10
cor = (200, 200, 200)

for i in range(num_bolas):
    x = np.random.randint(0, img.shape[0])
    y = np.random.randint(0, img.shape[1])

    img = desenha_circulo(img, build_circulo(x, y, raio), cor)

plt.imshow(img)
plt.show()
