import requests
import datetime
import os
basepath = '/Users/zkp/Desktop/imgdownload/' + datetime.datetime.now().strftime('%Y-%m-%d')

if not os.path.exists(basepath):
    os.makedirs(basepath)

def load_page(url):
    response=requests.get(url)
    data=response.content
    return data

def get_image(path, imgname):
    image =load_page(path)
    with open(basepath + '/%s.jpeg' % imgname,'wb') as fb:
        fb.write(image)


for i in range(100):
    import time
    time.sleep(1)
    get_image('http://www.miitbeian.gov.cn/getVerifyCode?86', i)
