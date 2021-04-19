#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   01.multi_thread_craw.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/15 3:43 下午   Lita       1.0         None
"""
import threading
import time

import blog_spider


# 单线程就是这样爬取的
def single_thread():
    print("single_thread begin:")
    for url in blog_spider.urls:
        blog_spider.craw(url)
    print("single_thread end:")


# 多线程无序的顺序
def multi_thread():
    print("multi_thread begin:")
    threads = []
    for url in blog_spider.urls:
        threads.append(
            threading.Thread(target=blog_spider.craw, args=(url,))
        )
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print("multi_thread end:")


if __name__ == '__main__':
    start = time.time()
    single_thread()
    end = time.time()
    print("single thread cost:", end - start, "seconds")

    start = time.time()
    multi_thread()
    end = time.time()
    print("multi_ thread cost:", end - start, "seconds")
