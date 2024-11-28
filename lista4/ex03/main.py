from matplotlib import image
from matplotlib import pyplot as plt
from progress.bar import Bar

img = image.imread('stinkbug.png')
print("Shape:", img.shape)


def suaviza_retangulo(img):
    new_img = img.copy()
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            media = (
                img[i - 1, j - 1] + img[i - 1, j] + img[i - 1, j + 1] +
                img[i,     j - 1] + img[i,     j] + img[i,     j + 1] +
                img[i + 1, j - 1] + img[i + 1, j] + img[i + 1, j + 1]
            ) / 9

            new_img[i, j] = media

    return new_img

def suaviza_cruz(img):
    new_img = img.copy()

    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            media = (
                img[i][j] +
                img[i - 1][j] +
                img[i + 1][j] +
                img[i][j - 1] +
                img[i][j + 1]
            ) / 5

            new_img[i][j] = media

    return new_img

img_suave = img
bar = Bar("Suavizando...", max=10)
for i in range(10):
    img_suave = suaviza_retangulo(img_suave)
    bar.next()
bar.finish()

fig = plt.figure()

ax = fig.add_subplot(1, 2, 1)
ax.imshow(img)

ax2 = fig.add_subplot(1, 2, 2)
ax2.imshow(img_suave)

plt.show()
