import cv2
# import os
import datetime
import os
import uuid
basepath = '/Users/zkp/Desktop/imgdownload/'
if not os.path.exists(basepath):
    os.makedirs(basepath)

def img_process(img_path, img_file):
    img = cv2.imread(img_path + "/" + img_file)
    # cv2.imshow('img', img)
    im1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h3 = cv2.adaptiveThreshold(im1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 6)
    # cv2.imshow('h3', h3)
    # cv2.imwrite('h3.jpeg', h3)

    for i in range(0, len(h3)):
        for j in range(0, len(h3[0])):
            if h3[i, j] == 0:
                if h3[i + 1, j] == 255:
                    h3[i, j] = 255
                elif h3[i + 1, j] == 0:
                    if h3[i + 2, j] == 255:
                        h3[i: i +2, j] = 255

    # cv2.imshow('h4', h3)

    # cv2.imwrite('h4.jpeg', h3)


    # kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    # h3=cv2.erode(h3, kernel)

    image, contours, hierarchy = cv2.findContours(h3, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    image = cv2.bitwise_not(image)
    # cv2.imshow('img', image)
    remain = []
    remain_map = {}
    for i in range(0, len(contours)):
        area = cv2.contourArea(contours[i])

        # print(area)
        if area < 100:
            cv2.drawContours(image, [contours[i]], 0, 0, -1)
        else:
            x, y, w, h = cv2.boundingRect(contours[i])
            # print(x, y ,w, h)
            # newimage = image[y:y + h, x:x + w]
            # kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
            # newimage=cv2.dilate(newimage, kernel)
            # cv2.imwrite(str(x) + ".jpg", newimage)
            if w < 100:
                remain.append(x)
                remain_map[str(x)] = contours[i]
    cv2.imwrite(img_file, image)
    remain.sort()

    rcount = 0
    remove_list = []
    for i in range(len(remain)):
        x, y, w, h = cv2.boundingRect(remain_map[str(remain[i])])
        if rcount > x + w:
            remove_list.append(remain[i])
        else:
            rcount = x + w

    for obj in remove_list:
        remain.remove(obj)

    if len(remain) ==6:
        x = list(range(len(remain)))
        # print(x)
        for i in x:
            # print(i)
            x, y, w, h = cv2.boundingRect(remain_map[str(remain[i])])
            # print(x, y, w, h)
            newimage = image[y:y + h, x:x + w]
            # kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
            # newimage=cv2.dilate(newimage, kernel)
            img_true_path = basepath + "/" + img_file.split('.')[0][i]
            if not os.path.exists(img_true_path):
                os.makedirs(img_true_path)
            cv2.imwrite(img_true_path + "/" + img_file.split('.')[0] + "_" + str(uuid.uuid4()) + ".jpg", newimage)
            # cv2.imwrite()
    else:
        print(img_file)
        print(len(remain))
        x = list(range(len(remain)))
        # print(x)
        for i in x:
            # print(i)
            x, y, w, h = cv2.boundingRect(remain_map[str(remain[i])])
            # print(x, y, w, h)
            newimage = image[y:y + h, x:x + w]
            # kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
            # newimage=cv2.dilate(newimage, kernel)
            img_true_path = basepath + "/" + img_file.split('.')[0]
            if not os.path.exists(img_true_path):
                os.makedirs(img_true_path)
            cv2.imwrite(img_true_path + "/" + str(uuid.uuid4()) + ".jpg", newimage)


if __name__ == '__main__':

    img_path = '/Users/zkp/Desktop/img'
    for img_file in os.listdir(img_path):
        try:
            img_process(img_path, img_file)
        except Exception as e:
            # print(e)
            print(img_file)