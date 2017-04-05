# -*- coding:utf-8 -*-
# from novel_grab import novel_grab
from flask import Flask, request, render_template
import time
import threading
import json
import urllib.request, urllib.error

app = Flask(__name__)

novels = [  # fake array of posts
    {
        'id': 1,
        'name': '人民的民义',
        'from': 'http://test.demo.com',
        'state': 100,
        'download': '#',
    }
]


def index_novel(n):
    for i, m in enumerate(novels):
        if m["name"] == n:
            return i
    return -1


def add_item(n, f):
    id = index_novel(n)
    if id < 0:
        novels.append({"id": len(novels) + 1, "name": n, "from": f, "state": 0, "download": ""})
        return True, len(novels)-1
    else:
        return False, id


def start_thread(id):
    global novels
    for i in range(101):
        novels[id]['state'] = i
        time.sleep(0.1)
        print("%d -> %d" % (id, i))


@app.route('/update')
def update():
    return json.dumps(novels)


@app.route('/')
def index():
    url = request.query_string.decode('utf8')
    print(url)
    if not str(url).startswith('http'):
        url = "http://" + url
    try:
        urllib.request.urlopen(url, timeout=1000)
    except urllib.error.URLError or urllib.error.HTTPError as e:
        return render_template('index.html', name=url, urlerror=str(e.reason))
    ret, id = add_item(url, url)
    print(id)
    if ret:  # first add
        t = threading.Thread(target=start_thread, args=(id,))
        print(t)
        t.start()
        return render_template('index.html', sites=['http://www.aoyuge.com', 'http://book.zongheng.com'],
                               name=url, novels=novels)
    else:
        return render_template('index.html', alreadyid=novels[id]["id"],
                               sites=['http://www.aoyuge.com', 'http://book.zongheng.com'],
                               name=url, novels=novels)
    return "invalid."


if __name__ == '__main__':
    """
    insert d.weolee.com:888?   before your novel chapters index page.
    """
    app.run(host='0.0.0.0', debug=True, port=888)
