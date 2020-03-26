#-*- coding:utf8 -*-
from pyquery import PyQuery as pq
import urllib
from mail import send_mail
import requests


pre_url = "http://www.bphc.com.cn"
gao_hash = "/tmp/.html"
yewu_url = "http://www.bphc.com.cn/front/noroomstaff/planLists"
yewu_hash = "/tmp/.yewu"


# capture gonggao url
try:
    g_f = file(gao_hash, 'r')
    g_old = g_f.read()
    g_f.close()
except:
    g_old = None

g_ret = urllib.urlopen("%s/article/list/b02e7e29e33642f789e4d1e41db08b7d.html" % pre_url)
if ret.getcode() == 200:
    g_page = g_ret.read()
    d = pq(g_page)
    div = d('.publicity')
    ul = div('ul')
    a = ul('a')[0]
    url = a.get('href')
    h = ul('h2')[0]
    mess = h.text
    verify = url + mess
    g_new = str(hash(verify))

    if g_new != g_old or g_old == None:
        send_mail(mess, pre_url + url)
        requests.get("https://sc.ftqq.com/server酱密钥?text=公租房&desp=[%s](%s)" %(mess.encode('utf8'), pre_url + url))
        g_f = file(gao_hash, 'w')
        g_f.write(g_new)
        g_f.close()


# capture yewu url
try:
    y = file(yewu_hash , 'r')
    y_old = y.read()
    y.close()
except:
    y_old = None

y_ret = urllib.urlopen(yewu_url)
if ret.getcode() == 200:
    y_page = y_ret.read()
    y_new = str(hash(y_page))

    if y_new != y_old or y_old == None:
        send_mail('ZZZFFF', yewu_url)
        requests.get("https://sc.ftqq.com/server酱密钥?text=公租房&desp=[业务](%s)" % yewu_url)
        y_f = file(yewu_hash, 'w')
        y_f.write(y_new)
        y_f.close()
