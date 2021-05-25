#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   bucketSort.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/5/25 5:19 下午   Lita       1.0         None
"""
import random


def bucketSort(li=[]):
    min_ = min(li)
    max_ = max(li)
    d = max_ - min_
    buckets_list = [[] for _ in range(len(li))]
    for val in li:
        digit = int((val - min_) * (len(li) - 1) / d)
        buckets_list[digit].append(val)
    for i in range(len(buckets_list)):
        buckets_list[i].sort()

    sort_arr = []
    for bucket in buckets_list:
        for ele in bucket:
            sort_arr.append(ele)

    return sort_arr


# li = [random.random() for _ in range(10)]
li = list(range(10))
random.shuffle(li)
print(li)
print(bucketSort(li))
