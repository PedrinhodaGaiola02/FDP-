from matplotlib import image
from matplotlib import pyplot as plt
from progress.bar import Bar

img = image.imread(r"D:\Documents\GitHub\FDP-\lista4\processamento_imagens\ex03\stinkbug.png")
print("Shape:", img.shape)


def suaviza_retangulo(img):
    new_img = img.copy()

    def get_arredores(img, i, j):
        arredores = [img[i, j]]

        if i > 0:
            arredores.append(img[i - 1, j])
        if i < img.shape[0] - 1:
            arredores.append(img[i + 1, j])
        if j > 0:
            arredores.append(img[i, j - 1])
        if j < img.shape[1] - 1:
            arredores.append(img[i, j + 1])

        if i > 0 and j > 0:
            arredores.append(img[i - 1, j - 1])
        if i > 0 and j < img.shape[1] - 1:
            arredores.append(img[i - 1, j + 1])
        if i < img.shape[0] - 1 and j > 0:
            arredores.append(img[i + 1, j - 1])
        if i < img.shape[0] - 1 and j < img.shape[1] - 1:
            arredores.append(img[i + 1, j + 1])

        return arredores

    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            arredores = get_arredores(img, i, j)
            media = sum(arredores) / len(arredores)
            new_img[i, j] = media

    return new_img

def suaviza_cruz(img):
    new_img = img.copy()

    def get_arredores(img, i, j):
        arredores = [img[i, j]]

        if i > 0:
            arredores.append(img[i - 1, j])
        if i < img.shape[0] - 1:
            arredores.append(img[i + 1, j])
        if j > 0:
            arredores.append(img[i, j - 1])
        if j < img.shape[1] - 1:
            arredores.append(img[i, j + 1])

        return arredores

    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            arredores = get_arredores(img, i, j)
            media = sum(arredores) / len(arredores)
            new_img[i][j] = media

    return new_img

img_suave1 = img
bar = Bar("Suavizando cruz...", max=10)
for i in range(10):
    img_suave1 = suaviza_cruz(img_suave1)
    bar.next()
bar.finish()

img_suave2 = img
bar = Bar("Suavizando retangulo...", max=10)
for i in range(10):
    img_suave2 = suaviza_retangulo(img_suave2)
    bar.next()
bar.finish()

fig = plt.figure()

ax = fig.add_subplot(3, 1, 1)
ax.imshow(img)

ax2 = fig.add_subplot(3, 1, 2)
ax2.set_title("Suavizado cruz")
ax2.imshow(img_suave1)

ax3 = fig.add_subplot(3, 1, 3)
ax3.set_title("Suavizado retangulo")
ax3.imshow(img_suave2)

plt.show()
