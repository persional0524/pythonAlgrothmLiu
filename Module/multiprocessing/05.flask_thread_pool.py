#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   05.flask_thread_pool.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/19 5:21 下午   Lita       1.0         None
"""
import json
import time

import flask

# name 为当前文件名称
app = flask.Flask(__name__)


def read_file():
    time.sleep(0.1)
    return "file result"


def read_db():
    time.sleep(0.2)
    return "db result"


def read_api():
    time.sleep(0.3)
    return "api result"


# @ 定义连接
@app.route("/")
def index():
    result_file = read_file()
    result_db = read_db()
    result_api = read_api()

    return json.dumps({
        "result_file": result_file,
        "result_db": result_db,
        "result_api": result_api,
    })


if __name__ == '__main__':
    app.run()
