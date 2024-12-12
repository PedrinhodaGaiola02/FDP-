import numpy as np
from matplotlib import pyplot as plt
from matplotlib import image

img = image.imread(r"D:\Documents\GitHub\FDP-\lista4\processamento_imagens\ex04\concrete.jpg")

print("Shape:", img.shape)

canalA = img[:, :, 0]

centroX = img.shape[0] // 2
centroY = img.shape[1] // 2
raio = 100
recorte = canalA[(centroX-raio):(centroX+raio), (centroY-raio):(centroY+raio)]

fig = plt.figure()

ax = fig.add_subplot(1, 2, 1)
ax.set_title("Original")
ax.imshow(canalA)

ax2 = fig.add_subplot(1, 2, 2)
ax2.set_title("Recorte")
ax2.imshow(recorte)

plt.show()
