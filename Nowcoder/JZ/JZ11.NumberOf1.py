#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   JZ21.NumberOf1.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/5/24 11:25 下午   Lita       1.0         None
"""


def NumberOf1_v1(n):
    if n < 0:
        n = n & 0xffffffff
    res = 0
    while n:
        n = n & (n - 1)
        res += 1
    return res


def NumberOf1_v2(n):
    if n < 0:
        n = n & 0xffffffff
    res = 0
    while n:
        if n & 1:
            res += 1
        n = n >> 1
    return res


print(NumberOf1_v1(10))
print(NumberOf1_v2(10))
