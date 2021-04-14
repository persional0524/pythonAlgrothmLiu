#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   01-单任务.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/14 3:17 下午   Lita       1.0         None
"""
import time

"""
并发：在一段时间内"交替"去执行多个任务。（任务数量大于cpu的核心数）
例子：对于单核cpu处理多任务，操作系统轮流让"各个任务交替运行"。

并行：在一段时间内"真正同时一起"执行多个任务。（任务数量小于等于cpu的核心数量）
例子：对于多核cpu处理多任务，操作系统会给cpu的每个内核安排一个执行的任务。
多个内核是真正的一起同时执行多个任务。
这里注意多核cpu是并行的执行多任务，始终有多个任务一起执行。

进程（process）：是资源分配的最小单位，他是操作系进行资源分配和调度运行的基本单元。
通俗理解：一个正在运行的程序就是一个进程，例如：正在运行的qq，微信等，他们都是一个进程。

引入并发：就是提升程序运行的速度。
必备能力，高级别 + 高薪 = 避不开的话题
"""


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
    dance()
    sing()
