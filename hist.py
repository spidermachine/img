import cv2

img = cv2.imread('/Users/zkp/Downloads/getVerifyCode11.jpeg')
cv2.imshow('img', img)
im1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
equ = cv2.equalizeHist(img)

# hist = cv2.calcHist([im1], [0], None, [256], [0, 256])
# cv2.imshow('h', hist)
from matplotlib import pyplot as plt
# plt.plot(hist)
# plt.show()
# plt.hist(img.ravel(), 256, [0, 256])
# plt.show()
# plt.hist(img.ravel(),256,[0,256])
# plt.show()
# h3 = cv2.adaptiveThreshold(im1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 6)
# cv2.imshow('h3', h3)
# cv2.imwrite('h3.jpeg', h3)
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
# cv2.imshow('h4', h4)
# cv2.

# cv2.waitKey(0)