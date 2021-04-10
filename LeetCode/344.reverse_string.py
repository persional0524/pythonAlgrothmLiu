#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   344.reverse_string.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/10 3:03 下午   Lita       1.0         None
"""

"""
描述
reverse() 函数用于反向列表中元素。
语法
reverse()方法语法：
返回值
该方法没有返回值，但是会对列表的元素进行反向排序。
"""


def reverse_string_v1(s):
    for i in range(len(s) // 2):
        s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
    return s


def reverse_string_v2(s):
    return s.reverse()


s = list(['h', 'e', 'l', 'l', 'o'])
# print(reverse_string_v2(s))
reverse_string_v2(s)
print(s)
