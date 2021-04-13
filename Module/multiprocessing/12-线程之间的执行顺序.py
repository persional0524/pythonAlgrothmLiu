#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   12-线程之间的执行顺序.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/14 10:31 下午   Lita       1.0         None
"""
import threading as td
import time

"""
 类型   线程名称    状态
<Thread(Thread-1, started 123145452576768)>
<Thread(Thread-2, started 123145452576768)>
<Thread(Thread-3, started 123145452576768)>
<Thread(Thread-4, started 123145452576768)>
<Thread(Thread-5, started 123145452576768)>
"""


def task():
    time.sleep(1)
    # current_thread :获取当前线程对象
    thread = td.current_thread()
    print(thread)


if __name__ == '__main__':
    for i in range(5):
        sub_thread = td.Thread(target=task)
        sub_thread.start()

# 结论： 多线程之前是无序的，有操作系统调度的。
# 线程之间是无序的，是有cpu调度决定某个线程先还行的。

"""
进程和线程的对比：
1、关系对比
    1-线程依附再进程里面的，没有进程就没有线程
    2-一个进程默认提供一条线程，进程可以创建多个线程
    3-一个进程（主线程，子线程。。。）
2、区别对比
    1-创建进程的开销要比线程开销资源要大
    2-进程是操作系统资源分配的基本单元，线程是cpu调度的基本单元
    3-线程不能独立执行必须依附存在进程中
3、优缺点对比
    1-进程优缺点：
        优点：真正意义上的多核
        缺点：资源开销大
    2-线程优缺点：
        优点：资源开销小
        缺点：不能使用多核
"""
