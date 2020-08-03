import cv2
import numpy as np

img = cv2.imread('Lenna.png')


#RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

RR = np.zeros(img.shape) 
# 넘파이에서는 기본적으로 float 형태로 만들어지게 된다.

R = img[:,:, 2]
# Red 채널을 표현하기 위해

RR[:,:,2] = R / 255.0
# RR 의 R 채널을 덮어씌어주는데
# R의 형태가 지금 0~ 255 사이의 int 형태이기 때문에 255로 나누어준다.

cv2.imshow('src', img)

cv2.imshow('dest', RR)


cv2.waitKey()
cv2.destroyAllWindows()

