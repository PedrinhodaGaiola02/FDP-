from matplotlib import image
from matplotlib import pyplot as plt

img = image.imread(r"D:\Documents\GitHub\FDP-\lista4\processamento_imagens\ex01\stinkbug.png")


print(img.shape)

A = img[:, :, 0]

plt.imshow(img)
plt.show()

plt.imshow(A)
plt.show()

plt.imshow(A, cmap='hot')
plt.show()

plt.imshow(A, cmap='nipy_spectral')
plt.show()
