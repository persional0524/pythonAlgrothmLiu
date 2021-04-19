#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   blog_spider.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/15 3:31 下午   Lita       1.0         None
"""
import requests as rq
from bs4 import BeautifulSoup

urls = [
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1, 50 + 1)
]


# print(urls)

def craw(url):
    r = rq.get(url)
    print(url, len(r.text))


def craw_v2(url):
    r = rq.get(url)
    return r.text  # 文档内容还没有解析


def parse(html):
    # class="post-item-title"
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_="post-item-title")
    return [(link['href'], link.get_text()) for link in links]


# https://www.cnblogs.com/#p1 69388(有字节码，爬成功了，6w多行)
# craw(urls[0])

if __name__ == '__main__':
    for result in parse(craw_v2(urls[2])):
        print(result)
