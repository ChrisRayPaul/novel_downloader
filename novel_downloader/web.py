# -*- coding:utf-8 -*-
from novel_grab import novel_grab
from flask import Flask, request, render_template
import time

app = Flask(__name__)


@app.route('/')
def index():
    url = request.query_string.decode('utf8')
    print(url)
    ct = 10
    return render_template('index.html', count=ct)


if __name__ == '__main__':
    """
    insert novel.weolee.com?   before your novel chapters index page.
    """
    app.run(host='0.0.0.0', debug=True, port=80)
