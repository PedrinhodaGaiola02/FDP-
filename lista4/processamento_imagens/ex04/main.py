import numpy as np
from matplotlib import pyplot as plt
from matplotlib import image

img = image.imread(r"D:\Documents\GitHub\FDP-\lista4\processamento_imagens\ex04\concrete.jpg")

print("Shape:", img.shape)

canalA = img[:, :, 0]

## Core

limiar = 125
agregados = np.zeros(img.shape)
numAgregados = 0
for i in range(canalA.shape[0]):
    for j in range(canalA.shape[1]):
        if canalA[i][j] > limiar:
            numAgregados += 1
            agregados[i][j] = (255, 255, 255)
        else:
            agregados[i][j] = (0, 0, 0)

# Plot
print("Percentual de agregados: {:.2f}%".format((numAgregados / (canalA.shape[0] * canalA.shape[1])) * 100))
fig = plt.figure()

ax = fig.add_subplot(2, 2, 1)
ax.set_title("Original")
ax.imshow(canalA)

ax2 = fig.add_subplot(2, 2, 2)
ax2.set_title("Agregados")
ax2.imshow(agregados)

ax2 = fig.add_subplot(2, 2, 3)
ax2.set_title("Limiar L={0}".format(limiar))
ax2.plot(range(len(canalA[0])), canalA[0])
ax2.plot(range(len(canalA[0])), limiar * np.ones(len(canalA[0])))

plt.show()
