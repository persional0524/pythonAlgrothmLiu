#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   7.reverse_int.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/7 3:00 下午   Lita       1.0         None
"""


def reverse_int_v1(num):

    res = 0
    while num > 0:
        res = res * 10
        res += num % 10
        num = num // 10
    return res


print(reverse_int_v1(12300))