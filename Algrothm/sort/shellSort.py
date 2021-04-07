#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   shellSort.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/6 9:41 下午   Lita       1.0         None
"""


def shell_sort(li):
    d = len(li) // 2
    while d > 0:
        insert_sort_gqp(li, d)
        d = d // 2


def insert_sort_gqp(li, d):
    for i in range(1, len(li)):
        j = i - d
        key = li[i]
        while j >= 0 and li[j] > key:
            li[j + d] = li[j]
            j = j - d
        li[j + d] = key


mylist = list([16, 25, 39, 27, 12, 8, 45, 63])

shell_sort(mylist)
print(mylist)
