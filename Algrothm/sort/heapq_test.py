#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   heapq_test.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/8 12:29 下午   Lita       1.0         None
"""


import heapq


li = [9,5,7,8,2,6,4,1,2]
# create heap
heapq.heapify(li)
print(li)
#  heap add element
heapq.heappush()
#  heap add element
#  优先队列：一些元素的集合，pop操作每次执行都会从优先队列中弹出最大或者最小元素
heapq.heappop()