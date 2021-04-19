#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   04.thread_pool.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/19 4:40 下午   Lita       1.0         None
"""
import concurrent.futures

import blog_spider

# craw
with concurrent.futures.ThreadPoolExecutor() as pool:
    # blog_spider.urls --> 列表
    htmls = pool.map(blog_spider.craw_v2, blog_spider.urls)
    """
    zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
    如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
    zip 方法在 Python 2 和 Python 3 中的不同：在 Python 3.x 中为了减少内存，zip() 返回的是一个对象。如需展示列表，需手动 list() 转换。
    >>>a = [1,2,3]
    >>> b = [4,5,6]
    >>> c = [4,5,6,7,8]
    >>> zipped = zip(a,b)     # 打包为元组的列表
    [(1, 4), (2, 5), (3, 6)]
    >>> zip(a,c)              # 元素个数与最短的列表一致
    [(1, 4), (2, 5), (3, 6)]
    >>> zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
    [(1, 2, 3), (4, 5, 6)]
    """
    htmls = list(zip(blog_spider.urls, htmls))
    for url, html in htmls:
        print(url, len(html))
print("craw over")
# parse
with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    for url, html in htmls:
        # submit --> 一个一个提交的
        future = pool.submit(blog_spider.parse, html)
        # key = url ,好处--把future和url建立联系
        futures[future] = url

    # 有序
    # for future, url in futures.items():
    #     print(url, future.result())

    # 乱序
    for future in concurrent.futures.as_completed(futures):
        url = futures[future]
        print(url, future.result())
