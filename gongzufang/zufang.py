#-*- coding:utf8 -*-
# python3

from pyquery import PyQuery as pq
import urllib
from weixin_api.ops import *
import hashlib

pre_url = "http://www.bphc.com.cn"
gao_hash = "/tmp/.html"
yewu_url = "http://www.bphc.com.cn/front/noroomstaff/planLists"
yewu_hash = "/tmp/.yewu"


# capture gonggao url
try:
    g_f = open(gao_hash, 'r')
    g_old = g_f.read()
    g_f.close()
except:
    g_old = None

g_ret = urllib.request.urlopen("%s/article/list/b02e7e29e33642f789e4d1e41db08b7d.html" % pre_url)
if g_ret.getcode() == 200:
    g_page = g_ret.read()
    d = pq(g_page)
    div = d('.publicity')
    ul = div('ul')
    a = ul('a')[0]
    url = a.get('href')
    h = ul('h2')[0]
    mess = h.text
    verify = url + mess
    g_new = hashlib.md5(verify.encode('utf8')).hexdigest()

    if g_new != g_old or g_old == None:
        send_text(agentid, mess + '\n' + pre_url + url)
        g_f = open(gao_hash, 'w')
        g_f.write(g_new)
        g_f.close()


# capture yewu url
try:
    y = open(yewu_hash , 'r')
    y_old = y.read()
    y.close()
except:
    y_old = None

y_ret = urllib.request.urlopen(yewu_url)
if y_ret.getcode() == 200:
    y_page = y_ret.read()
    d = pq(y_page)
    div = d('.planContent')
    ul = div('h2')
    h = ul('h2')[0]
    mess = h.text
    y_new = hashlib.md5(mess.encode('utf8')).hexdigest()

    if y_new != y_old or y_old == None:
        send_text(agentid, 'ZZZFFF登记\n' + yewu_url)
        y_f = open(yewu_hash, 'w')
        y_f.write(y_new)
        y_f.close()


