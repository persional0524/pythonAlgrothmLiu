#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   08.asynic_spider.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/20 11:01 上午   Lita       1.0         None
"""
import asyncio
import time

import aiohttp

import blog_spider

"""
协程是什么，异步io里面执行的函数，他和普通的函数的不同，
他是需要超级循环调度的
"""


# 异步的需要在前面添加 async 关键字
async def async_craw(url):
    print("craw url:", url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            # await 超级循环不会一直等待，而已直接切换写下一个URL的爬取,resp.text()获取结果
            result = await resp.text()
            print(f"craw url :{url},{len(result)}")


# 获取事件循环，超级循环
loop = asyncio.get_event_loop()
# 创建task列表,50个博客园的列表
tasks = [
    loop.create_task(async_craw(url))
    for url in blog_spider.urls]

start = time.time()
# 执行爬虫事件列表,等待所有的task的执行完成
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print("use time seconds:", end - start)
