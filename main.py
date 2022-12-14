import cv2
import matplotlib.pyplot as plt
import numpy as np


def stack(*args):
    return np.hstack(args)


def rescale(foto):
    s = foto.astype(float)
    s -= np.min(s)
    s /= np.max(s)
    return (s*255).astype(np.uint8)


def kuvvet_donusumu(r, c, gamma):
    r = r.astype(float)
    s = c*r**gamma
    s = rescale(s)
    return s


def main():

    foto = cv2.imread("sehir.jpeg")
    c = 1
    gamma_degerleri = [3, 4, 5]
    kuvvet_fotolari = []
    for gamma in gamma_degerleri:
        kuvvet_foto = kuvvet_donusumu(foto, c=c, gamma=gamma)
        kuvvet_fotolari.append(kuvvet_foto)


    satir1 = stack(foto, kuvvet_fotolari[0])
    satir2 = stack(*kuvvet_fotolari[1:])

    grid = np.vstack((satir1, satir2))


    plt.imshow(grid, cmap="gray")
    plt.show()



if __name__ == "__main__":
    main()

