#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   10-线程执行带有参数的任务.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/14 10:21 下午   Lita       1.0         None
"""
import threading as td
import time


# 跳舞
def dance(num, name):
    for i in range(num):
        print(name)
        print("跳舞...")
        time.sleep(0.5)


# 唱歌
def sing(num, name):
    for i in range(num):
        print(name)
        print("唱歌...")
        time.sleep(0.5)


if __name__ == '__main__':
    # 2、使用进程类创建对象
    # target：指定进程执行的函数名
    # args：使用元组的方式给指定任务传参数
    # kwargs：使用字典的方式给指定的任务传参数
    sing_thread = td.Thread(target=sing, args=(3, "xiaoming"))
    dance_thread = td.Thread(target=dance, kwargs={"name": 'liutao', "num": 2})
    # 3、使用进程对象启动进程执行指定任务
    sing_thread.start()
    dance_thread.start()
