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

"""
基数排序只能处理正整数，做多少次，和最大次的位数有关系
非比较排序。比较排序中最快nlogn
"""


def get_diget(num, i):
    # i=0,个位 1 十位 2 百位
    # 57841:0-->1, 1-->4, 2-->8, 3-->7, 4-->5
    return num // (10 ** i) % 10


# 数字转换列表 12345 --> [1,2,3,4,5]
def int2str(num):
    li = []
    while num > 0:
        li.append(num % 10)
        num //= 10
        li.reverse()  # 反转
    return li


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
print(get_diget(57841, 2))
print(int2str(57841))
