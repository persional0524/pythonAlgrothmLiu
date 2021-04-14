# !/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   11-主线程和子线程的结束顺序.py
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/14 10:14 下午   Lita       1.0         None
"""

"""
主线程和子线程结束的顺序：
1、主线程会等待所有的子线程结束再结束，除非设置子线程守护主线程
2、设置守护线程有两种方式：
     (1)、theading.Thread(target=work,daemon=True)
     (2)、线程对象setDaemon(True)
     (3)、一定在启动线程之前
     
"""

import threading as td
import time


def work():
    for i in range(10):
        print("work...")
        time.sleep(0.2)


if __name__ == '__main__':
    # 主线程结束不想等待子线程结束再结束，可以设置守护线程
    # sub_thread = td.Thread(target=work,daemon=True)
    sub_thread = td.Thread(target=work)
    sub_thread.setDaemon(True)
    sub_thread.start()

    time.sleep(1)
    print("主进程执行完成...")
