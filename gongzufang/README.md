用于抓取公租房公告信息，及时通知自己能尽快办理相关租房业务；致北漂！！！

1. 依赖pyquery
      pip3 install pyquery
      pip3 install -e git+https://github.com/007root/weixin_api.git#egg=weixin_api
2. 添加定时任务
    */5 * * * * /usr/bin/python3 /home/zufang/zufang.py
