#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   02.producer_consumer_spider.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/19 2:08 下午   Lita       1.0         None
"""
import queue
import random
import threading
import time

import blog_spider


# 生产者
def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):
    while True:
        url = url_queue.get()
        html = blog_spider.craw_v2(url)
        html_queue.put(html)
        """
        list_ = [1,2,3]
        print(list_, f'has a length of {len(list_)}.')
        # [1,2,3] has a length of 3.
        
        print(list_, f'has a length of {{len(list_)}}.')
        # [1,2,3] has a length of {len(list_)}.
        
        print(list_, f'has a length of {{{len(list_)}}}.')
        # [1,2,3] has a length of {3}.

        """
        # 打印当前线程的名字，f-string: formatted string literals, 格式化字符串常量。功能同str.format() %-formatting,
        # 较两者更简洁易用，推荐使用
        # 需要注意的是，Python3.6及以后的版本可用。
        print(threading.current_thread().name, f"craw_2-{url}",
              "url_queue.size=", url_queue.qsize())
        # 随机睡眠1-2s
        time.sleep(random.randint(1, 2))


def do_parse(html_queue: queue.Queue, fout):
    while True:
        html = html_queue.get()
        results = blog_spider.parse(html)
        for result in results:
            fout.write(str(result) + "\n")
        print(threading.current_thread().name, f"results.size", len(results),
              "html_queue.size=", html_queue.qsize())
        # 随机睡眠1-2s
        time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    # 启动生产者线程
    for url in blog_spider.urls:
        url_queue.put(url)

    # 启动3个生产者线程
    for idx in range(3):
        t = threading.Thread(target=do_craw, args=(url_queue, html_queue),
                             name=f"craw_v2{idx}")
        t.start()

    # 启动2个消费者线程
    fout = open("02.data.txt", "w")
    for idx in range(2):
        t = threading.Thread(target=do_parse, args=(html_queue, fout),
                             name=f"parse{idx}")
        t.start()
