from matplotlib import image
from matplotlib import pyplot as plt

img = image.imread('stinkbug.png')
print("Shape:", img.shape)

def suaviza(img):
    return img

plt.imshow(suaviza(img))
plt.show()
