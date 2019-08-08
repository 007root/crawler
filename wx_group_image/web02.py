# -*- coding:utf8 -*-
"""
pip3 install lxml
sudo apt update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
wget https://github.com/tesseract-ocr/tessdata/blob/master/chi_sim.traineddata
"""
import requests
from bs4 import BeautifulSoup
import bs4
import xlwt
from hashlib import md5
import os
import re
from datetime import datetime
import random
from baidu import get_image_text
from weixin_api.ops import agentid, send_image
import time
import random
time.sleep(random.randint(20,160))


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3071.115 Safari/538.36'}
date_re = re.compile(r'[0-9]{4}-[0-9]{2}-[0-9]{2}')
today = datetime.today()

def gethtml(url):
    proxys = [
        {"http": "http://192.168.4.252:10000"},
        {"http": "http://192.168.4.252:10001"},
        {"http": "http://192.168.4.252:10002"},
    ]
    try:
        html = requests.get(url,headers=headers,timeout=30)
        html.raise_for_status()
        html.encoding = html.apparent_encoding
        return html.text
    except Exception as e:
        print(e)
        print('get html fail')
        raise


def getchaturls(html, g_num):
    g_dict = {
        "g_02_div": "dt",
        "g_02_url": "http://www.gpwxq.com"
    }
    div = g_dict[g_num + '_div']
    url = g_dict[g_num + '_url']
    try:
        soup = BeautifulSoup(html,'html.parser')
        chat_url = []
        if soup:
            count = 0
            for chat in soup.find_all('div',class_=div):
                count += 1
                if count > 20: break
                if count > 10:
                    chat = chat.img.attrs['src']
                    chat_url.append(url+chat)
                else:
                    continue
            return chat_url
    except Exception as e:
        print('get every page info fail')
        raise


def getinfo(url):
    for i in url:
        i = i.replace('Uploads/../../..//', '')
        print(i)
        savepic(i)
    return True


def savepic(url):
    '''save QR code'''
    path = '/home/ubuntu/code/weixin/images/'
    if not os.path.exists(path):
        os.mkdir(path)
    if checkgroup(url):
        try:
            ret = requests.get(url,headers=headers)
        except:
            print('retry>>>')
            ret = requests.get(url,headers=headers)
        photo = ret.content
        print('pho')
        filename = md5(photo).hexdigest()
        if not os.path.isfile(path + filename):
            send_image(agentid, photo)
            os.popen('touch %s%s' % (path, filename))


def checkgroup(url):
    result = get_image_text(url)
    words_list = result.get('words_result')
    if words_list:
        for i in words_list:
            text = i.get('words')
            if "群" in text or "交流" in text or "该二" in text or "效" in text or "更新" in text:
                return True


def main():
    page = 1
    while True:
        g_02 = "http://www.gpwxq.com/weixin-index-id-44-p-{}.html"
        first_url = g_02.format(page)
        print('current {} page,url: {}'.format(page,first_url))
        html = gethtml(first_url)
        urls = getchaturls(html, 'g_02')
        st = getinfo(urls)
        if st:
            print('=====finished=====')
            return
        page += 1

if __name__=='__main__':
    main()

