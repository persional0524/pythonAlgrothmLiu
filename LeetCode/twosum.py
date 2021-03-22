#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   twosum.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/22 9:42 下午   Lita       1.0         None
"""


def twosum_v1(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if target == arr[i] + arr[j]:
                return [i, j]
    return []


my_list = ([2, 15, 11, 7])
print(twosum_v1(my_list, 9))
