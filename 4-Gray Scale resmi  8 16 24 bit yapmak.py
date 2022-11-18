import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
img=cv2.imread("bmw1.jpeg",0)
print(img.dtype)
cv2.imshow("gray",img)
x=np.min(img)
y=np.max(img)
print("min:",x)
print("max:",y)
print(img)

def donusum(img):# 16 bit
    s=img.astype(float)
    s-=np.min(s)
    s/=np.max(s)
    return (s*65535)  # 2^32,2^64 ....
img=donusum(img)
x=np.min(img)
y=np.max(img)
print("min:",x)
print("max:",y)
print(type(img))
print(img)
cv2.imshow("donusturulmus",img)
cv2.waitKey(0)