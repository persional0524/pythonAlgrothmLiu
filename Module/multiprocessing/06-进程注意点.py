#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   06-进程注意点.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/14 5:53 下午   Lita       1.0         None
"""

"""
主进程会等待所有子进程执行结束再结束
* 为了保证子进程能够正常的运行，主进程会等所有的子进程执行完毕后再销毁，
* 设置守护进程的目的是主进程退出子进程销毁，不让主进程再等待子进程去执行。
* 设置守护进程的方式：子进程对象.daemon = True
"""

import multiprocessing
import time


def work():
    # 子进程工作2秒
    for i in range(10):
        print("工作中...")
        time.sleep(0.2)


if __name__ == '__main__':
    work_process = multiprocessing.Process(target=work, daemon=True)  # 守护进程
    # work_process = multiprocessing.Process(target=work)
    work_process.start()
    # 主进程睡眠1秒
    time.sleep(1)
    print("主进程执行完成...")
