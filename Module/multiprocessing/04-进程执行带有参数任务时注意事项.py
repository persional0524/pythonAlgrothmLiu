#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   04-进程执行带有参数任务时注意事项.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/14 4:50 下午   Lita       1.0         None
"""
# 1、 导入进程包
import multiprocessing as mp
import os
import time


# 跳舞
def dance(num, name):
    print("跳舞进程pid：", os.getgid())
    for i in range(num):
        print(name)
        print("跳舞...")
        time.sleep(0.5)


# 唱歌
def sing(num, name):
    print("唱歌进程pid：", os.getgid())
    for i in range(num):
        print(name)
        print("唱歌...")
        time.sleep(0.5)


if __name__ == '__main__':  # 主进程
    # 2、使用进程类创建对象
    # target：指定进程执行的函数名
    # args：使用元组的方式给指定任务传参数
    # kwargs：使用字典的方式给指定的任务传参数

    """创建子进程对象并指定执行的任务名"""
    sing_prcess = mp.Process(target=sing, args=(3, "xiaoming"))
    dance_prcess = mp.Process(target=dance, kwargs={"name": 'liutao', "num": 2})
    # 3、使用进程对象启动进程执行指定任务-启动子进程并执行任务
    sing_prcess.start()
    dance_prcess.start()
