#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   radixSort.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/6 12:22 下午   Lita       1.0         None
"""


def radixSort_v1(arr=[]):
    max_v = max(arr)
    i = 0
    while 10 ** i <= max_v:
        # 10 buckets
        buckets = [[] for _ in range(10)]
        for val in arr:
            digit = val // (10 ** i) % 10
            print("digit=" + str(digit))
            buckets[digit].append(val)
        arr.clear()
        print(buckets)
        for bucket in buckets:
            for element in bucket:
                arr.append(element)
        i += 1
    return arr


mylist = list([16, 25, 39, 27, 12, 8, 45, 63])
print(radixSort_v1(mylist))


