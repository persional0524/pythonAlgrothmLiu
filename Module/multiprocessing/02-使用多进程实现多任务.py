#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   02-使用多进程实现多任务.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/14 3:18 下午   Lita       1.0         None
"""
# 1、 导入进程包
import multiprocessing as mp
import time


# 跳舞
def dance():
    for i in range(3):
        print("跳舞...")
        time.sleep(0.5)


# 唱歌
def sing():
    for i in range(3):
        print("唱歌...")
        time.sleep(0.5)


if __name__ == '__main__':
    # 2、使用进程类创建对象
    # target：指定进程执行的函数名
    sing_prcess = mp.Process(target=sing)
    dance_prcess = mp.Process(target=dance)
    # 3、使用进程对象启动进程执行指定任务
    sing_prcess.start()
    dance_prcess.start()
