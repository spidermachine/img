import cv2

img = cv2.imread('/Users/zkp/Downloads/getVerifyCode11.jpeg')
cv2.imshow('img', img)
im1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h3 = cv2.adaptiveThreshold(im1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 6)
cv2.imshow('h3', h3)
cv2.imwrite('h3.jpeg', h3)
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
h4=cv2.dilate(h3, kernel)
# cv2.imshow('h4', h4)
# cv2.

image, contours, hierarchy = cv2.findContours(h4, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

image = cv2.bitwise_not(image)
# cv2.imshow('img', image)
for i in range(0, len(contours)):
    area = cv2.contourArea(contours[i])

    print(area)
    if area < 100:
        cv2.drawContours(image, [contours[i]], 0, 0, -1)
    # else:
    #     x, y, w, h = cv2.boundingRect(contours[i])
    #     print(x, y, w, h)
    #     newimage = image[y :y + h , x :x + w ]
    #     cv2.imwrite(str(i) + ".jpg", newimage)




cv2.imshow('result', image)

image = cv2.dilate(image, kernel)
cv2.imshow('result1', image)

image, contours, hierarchy = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# image = cv2.bitwise_not(image)
# cv2.imshow('img', image)
for i in range(0, len(contours)):
    area = cv2.contourArea(contours[i])

    print(area)
    if area < 100:
        cv2.drawContours(image, [contours[i]], 0, 0, -1)
    else:
        x, y, w, h = cv2.boundingRect(contours[i])
        print(x, y, w, h)
        newimage = image[y :y + h , x :x + w ]
        cv2.imwrite(str(i) + ".jpg", newimage)

cv2.waitKey(0)