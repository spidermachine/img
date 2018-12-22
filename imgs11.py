import cv2
import os
import uuid
basepath = './imgdownload/'
if not os.path.exists(basepath):
    os.makedirs(basepath)

def img_process(img_path, img_file):
    img = cv2.imread(img_path + "/" + img_file)
    im1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h3 = cv2.adaptiveThreshold(im1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 6)

    for i in range(0, len(h3) - 2):
        for j in range(0, len(h3[0])):
            if h3[i, j] == 0:
                if h3[i + 1, j] == 255:
                    h3[i, j] = 255
                elif h3[i + 1, j] == 0:
                    if h3[i + 2, j] == 255:
                        h3[i: i + 2, j] = 255
    h3[:, 0] = 255
    h3[:, len(h3[0]) - 1] = 255
    h3[1, :] = 255
    h3[len(h3) - 1, :] = 255

    # reduce_noise(h3, 1)
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
            x, y, w, h = cv2.boundingRect(contours[i])
            # print x, y, w, h
        else:
            x, y, w, h = cv2.boundingRect(contours[i])

            print(x, y, w, h)
            if x > 0:
                if w >= 35:
                    need_split = True
                remain.append(x)
                remain_map[str(x)] = (x, y, w, h)

    cv2.imwrite(img_file, image)
    remain.sort()

    print len(remain)
    rcount = 0
    remove_list = []
    # if len(remain) != 6:
    for i in range(len(remain)):
        x, y, w, h = remain_map[str(remain[i])]
        if rcount > x + w:
            remove_list.append(remain[i])
        else:
            rcount = x + w


    for obj in remove_list:
        remain.remove(obj)

    remain_list = []
    remove_list = []
    add_map = {}

    for x in remain:
        remain_list.append(remain_map[str(x)])

    print(len(remain))

    for i in range(len(remain_list)):
        x, y, w, h = remain_list[i]
        if i < len(remain_list) - 1:
            xx, yy, ww, hh = remain_list[i + 1]

            if w + ww <= 35 and abs(x + w - xx) <= 4:
                remain_list[i] = (x, y, w + ww, h)
                remove_list.append((xx, yy, ww, hh))

        if w > 70:
            wn = int(w/3)
            add_map[str(i)] = (x, y, wn, h)
            add_map[str(i + 1)] = (x + wn, y, wn, h)
            add_map[str(i + 2)] = (x + 2 * wn, y, wn, h)
            remove_list.append((x, y, w, h))

        if (w >= 35) and (w <= 70):
            wn = int(w/2)
            add_map[str(i)] = (x, y, wn, h)
            add_map[str(i + 1)] = (x + wn, y, wn, h)
            remove_list.append((x, y, w, h))


    for k, v in add_map.items():
        remain_list.insert(int(k), v)

    for i in remove_list:
        remain_list.remove(i)

    # for k, v in remain_map.items():
    #     x, y, w, h = cv2.boundingRect()
    remove_list = []
    remain = None
    remove_list = None
    print remain_list, len(remain_list)
    if len(remain_list) ==6:
        # print(x)
        for i in range(len(remain_list)):
            # print(i)
            x, y, w, h = remain_list[i]
            print(x, y, w, h)
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
        for i in range(len(remain_list)):
            # print(i)
            x, y, w, h = remain_list[i]
            print(x, y, w, h)
            # if w > 35:

            newimage = image[y:y + h, x:x + w]
            # kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
            # newimage=cv2.dilate(newimage, kernel)
            img_true_path = basepath + "/" + img_file.split('.')[0]
            if not os.path.exists(img_true_path):
                os.makedirs(img_true_path)
            cv2.imwrite(img_true_path + "/" + str(uuid.uuid4()) + ".jpg", newimage)


def reduce_noise(img, ths):
    for i in range(0, len(img)):
        if len(img[i]) - sum(img[i])/255 < ths:
            img[i, :] = 255

    for i in range(0, len(img[0])):
        if len(img) - sum(img[:, i])/255 < ths:
            img[:, i] = 255


if __name__ == '__main__':

    img_path = 'img'
    img_process(img_path, 'H7Q458.jpeg')
