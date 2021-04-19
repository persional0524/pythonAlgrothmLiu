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
from concurrent.futures import ThreadPoolExecutor

import flask

# name 为当前文件名称
app = flask.Flask(__name__)
# 初始化一个全局线程池
pool = ThreadPoolExecutor()


def read_file():
    time.sleep(0.1)
    return "file result"


def read_db():
    time.sleep(0.2)
    return "db result"


def read_api():
    time.sleep(0.3)
    return "api result"


# @ 定义连接,接口
@app.route("/")
def index():
    # result_file = read_file()
    # result_db = read_db()
    # result_api = read_api()
    # return json.dumps({
    #     "result_file": result_file,
    #     "result_db": result_db,
    #     "result_api": result_api,
    # })
    result_file = pool.submit(read_file)
    result_db = pool.submit(read_db)
    result_api = pool.submit(read_api)
    # future 对象 -->  .result()
    return json.dumps({
        "result_file": result_file.result(),
        "result_db": result_db.result(),
        "result_api": result_api.result(),
    })


if __name__ == '__main__':
    app.run()
