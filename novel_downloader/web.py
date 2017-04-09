# -*- coding:utf-8 -*-
# from novel_grab import novel_grab
from flask import Flask, request, render_template
import time
import threading
import json
import urllib.request, urllib.error
import os, sys

os.chdir(os.path.join(sys.path[0], "static"))

from novel_grab.novel_grab import Downloader

app = Flask(__name__, static_url_path="")
sites=['http://www.aoyuge.com', 'http://book.zongheng.com','http://www.quanshu.net']
novels = [  # fake array of posts
    {
        'id': 1,
        'name': '星际穿梭商店 作者：忘记二少',
        'from': 'http://www.aoyuge.com/32/32363/index.html',
        'state': 100,
        'download': '星际穿梭商店 作者：忘记二少.7z',
    },
    {
        'id': 2,
        'name': '校园小神医 作者：伤贤梦魂',
        'from': 'http://book.zongheng.com/showchapter/648323.html',
        'state': 100,
        'download': '校园小神医 作者：伤贤梦魂.7z',
    },
    {
        'id': 3,
        'name': '大刁民 作者：仲星羽',
        'from': 'http://book.zongheng.com/showchapter/43467.html',
        'state': 100,
        'download': '大刁民 作者：仲星羽.7z',
    }
]


def index_novel(u):
    for i, m in enumerate(novels):
        if m["from"] == u:
            return i
    return -1


def add_item(n, f, d):
    id = index_novel(f)
    if id < 0:
        novels.append({"id": len(novels) + 1, "name": n, "from": f, "state": 0, "download": d})
        return True, len(novels) - 1
    else:
        return False, id


@app.route('/update')
def update():
    if grab:
        if grab.info["id"]:
            novels[grab.info["id"]]['state'] = "%d" % grab.get_info()["percent"]
            novels[grab.info["id"]]['name'] = grab.get_info()["novel_name"]
    return json.dumps(novels)


grab = None


@app.route('/')
def index():
    global grab
    url = request.query_string.decode('utf8')
    print(url)
    if not str(url).startswith('http'):
        url = "http://" + url
    try:
        urllib.request.urlopen(url, timeout=1000)
    except urllib.error.URLError or urllib.error.HTTPError as e:
        return render_template('index.html', name=url, urlerror=str(e.reason))
    nid = index_novel(url)
    if nid < 0:  # first add
        grab = Downloader(url)
        grab.info["url"] = url
        threading.Thread(target=grab.start).start()
        _, grab.info["id"] = add_item(n=grab.get_info()["novel_name"], f=url, d=grab.get_info()["file_name"])
        print(grab.get_info())
        return render_template('index.html', sites=sites,
                               name=url, novels=novels)
    else:

        return render_template('index.html', alreadyid=nid + 1, sites=sites,
                               name=url, novels=novels)
    return "invalid."


if __name__ == '__main__':
    """
    insert d.weolee.com:777?   before your novel chapters index page.
    """
    app.run(host='0.0.0.0', debug=True, port=777)
