import cv2
import matplotlib.pyplot as plt

# Resmi okutuyoruz
img_bgr = cv2.imread('doga.jpeg', 1)
plt.imshow(img_bgr)
plt.show()


# görüntünün yüksekliğini ve genişliğini alıyoruz
height, width, _ = img_bgr.shape

for i in range(0, height - 1):
    for j in range(0, width - 1):
        # pixel değeri alıyoruz
        pixel = img_bgr[i, j]

        # her kanalı negative çeviriyoruz
        # 255 ten eksilterek

        # 1. dizi kırmızı
        pixel[0] = 255 - pixel[0]

        # 2. dizi yeşil
        pixel[1] = 255 - pixel[1]

        # 3. dizi mavi
        pixel[2] = 255 - pixel[2]

        # yeni değerleri pixele atıyoruz
        img_bgr[i, j] = pixel

# Negatif dönüştürülmüş görüntü gösterimi
cv2.imshow("Original Image", img_bgr)

plt.imshow(img_bgr)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

