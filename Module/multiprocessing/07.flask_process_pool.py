#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   07.flask_process_pool.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/20 9:09 上午   Lita       1.0         None
"""
import json
import math
from concurrent.futures import ProcessPoolExecutor

import flask


app = flask.Flask(__name__)


# cpu 密集型计算

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


# 接口
@app.route("/is_prime/<numbers>")
def api_is_prime(numbers):
    number_list = [int(x) for x in numbers.split(",")]
    results = process_pool.map(is_prime, number_list)
    return json.dumps(dict(zip(number_list, results)))


""""
多进程和多线程的区别：
    多进程的环境是完全隔离的，有一点限制，就是当你定义这个pool的时候，他所依赖的这些函数必须都已经声明完了。
    所以说着暗含什么意思那？
    process_pool = ProcessPoolExecutor() 必须放在所有的函数声明的最下面才能正常使用.
    大部分用多线程就ok，遇到cpu密集型计算，得想办法引用多进程来解决问题使用它
    
    flask程序中就是在"main"函数中，app的run之前初始化这个pool

"""
if __name__ == '__main__':
    process_pool = ProcessPoolExecutor()
    app.run()
