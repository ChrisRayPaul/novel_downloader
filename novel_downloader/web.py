# -*- coding:utf-8 -*-
from novel_grab import novel_grab
from flask import Flask, request, render_template
import time
import threading

app = Flask(__name__)

novels = [  # fake array of posts
    {
        'id': 1,
        'name': 'Beautiful day in Portland!',
        'from': 'ffff',
        'state': 0,
        'download': 'xxx',
    },
    {
        'id': 2,
        'name': 'aaa day in Portland!',
        'from': 'ffff2',
        'state': 100,
        'download': 'ccc',
    }
]


def start_thread(url):
    global novels
    for i in range(11):
        novels[0]['state'] = i*10
        time.sleep(1)


cache = {}


@app.route('/')
def index():
    global cache
    url = request.query_string.decode('utf8')
    if url not in cache:
        t = threading.Thread(target=start_thread, args=(url,))
        t.start()
        cache[url] = 0
    return render_template('index.html', name=url, novels=novels)


if __name__ == '__main__':
    """
    insert novel.weolee.com?   before your novel chapters index page.
    """
    app.run(host='0.0.0.0', debug=True, port=80)
