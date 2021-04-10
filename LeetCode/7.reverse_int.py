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
        print(res)
        res += num % 10
        print(" " + str(res))
        num = num // 10
        print("  " + str(num))
    return res


def reverse_int_v2(x):
    if -10 < x < 10:
        return x
    str_x = str(x)
    if str_x[0] != "-":
        str_x = str_x[::-1]
        print(str_x)
        x = int(str_x)
    else:
        str_x = str_x[:0:-1]
        print(str_x)
        x = int(str_x)
        x = -x
    return x if -2147483648 < x < 2147483647 else 0


print(reverse_int_v2(-12300))
