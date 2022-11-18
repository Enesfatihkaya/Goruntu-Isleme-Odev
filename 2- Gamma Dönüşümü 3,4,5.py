import cv2
import numpy as np


img = cv2.imread('bmw1.jpeg')

# gama degerleri
for gamma in [3, 4, 5]:
    # gamma donusum uygulanması
    gamma_donusum = np.array(255 * (img / 255) ** gamma, dtype='uint8')

    # donusturulen resimlerin kaydedilmesi
    cv2.imwrite('gammadonusum_bmw' + str(gamma) + '.jpg', gamma_donusum)

