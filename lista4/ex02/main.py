from matplotlib import image
from matplotlib import pyplot as plt

img = image.imread('stinkbug.png')

print(img.shape)
# print(img)

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

# img = listras(img)

img = desenha_circulo(img, build_circulo(100, 100, 50), (0, 0, 0))
img = desenha_circulo(img, build_circulo(200, 200, 100), (255, 255, 255))
img = desenha_circulo(img, build_circulo(100, 400, 80), (0, 255, 0))

plt.imshow(img)
plt.show()
