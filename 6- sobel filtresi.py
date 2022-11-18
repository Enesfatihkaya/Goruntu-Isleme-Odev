import cv2
import numpy as np


from matplotlib import pyplot as plt

# resmi yüklüyoruz
img = cv2.imread('bmw1.jpeg',)

# griye çeviriyoruz
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# gürültüyü kaldırıyoruz
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)



#sobel
img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=5)
img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=5)
img_sobel = img_sobelx + img_sobely





cv2.imshow("Original Image", img)
cv2.imshow("Sobel X", img_sobelx)
cv2.imshow("Sobel Y", img_sobely)
cv2.imshow("Sobel", img_sobel)


cv2.waitKey(0)
cv2.destroyAllWindows()