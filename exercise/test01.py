#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   test01.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/29 9:22 上午   Lita       1.0         None
"""

import random


def foo(n):
    random.seed()
    c1 = 0
    c2 = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        r1 = x * x + y * y
        r2 = (1 - x) * (1 - x) + (1 - y) * (1 - y)
        if r1 <= 1 and r2 <= 1:
            c1 += 1
        else:
            c2 += 1
    return c1 / c2


str = "Hello,Python";
suffix = "Python";
print(str.endswith(suffix, 2));
