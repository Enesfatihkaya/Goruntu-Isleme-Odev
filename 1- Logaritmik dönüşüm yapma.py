import cv2
import numpy as np
import matplotlib.pyplot as plt
#logaritmik dönüşüm koyu pixel değerlerini yükselteceğinden dolayı görüntüyü iyileştirmek amacıyla kullanılır.
# resmi okuyoruz
img = cv2.imread('bmw1.jpeg')

# logaritma dönüşüm formülümüzü ekliyoruz
# burada  r -> giriş pixel değeri c->ölçekleme sabiti s -> çıkış pixel değeri
# herhangi bir pixel 0 olursa eğer log sonsuz olacağından pixel değerlerine 1 ekliyoruz.

c = 255 / np.log(1 + np.max(img))
log_image = c * (np.log(img + 1))

# float değeri int çeviriyoruz
log_image = np.array(log_image, dtype=np.uint8)

# resim gösterimi
cv2.imshow("Original Image", img)
cv2.imshow("log dönüşümlü Image", log_image)


cv2.waitKey(0)
cv2.destroyAllWindows()