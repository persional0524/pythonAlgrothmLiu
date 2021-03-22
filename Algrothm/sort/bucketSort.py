#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   bucketSort.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/22 9:57 下午   Lita       1.0         None
"""


def bucket_sort_v1(arr=[]):
    max_v = arr[0]
    min_v = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_v:
            max_v = arr[i]
        if arr[i] < min_v:
            min_v = arr[i]
    d = max_v - min_v
    bucket_num = len(arr)
    bucket_list = []
    for i in range(len(arr)):
        bucket_list.append([])
    for i in range(len(arr)):
        num = int((arr[i] - min_v) * (bucket_num - 1) / d)
        print("bucket_list=" + str(bucket_list))
        print("num=" + str(num))
        bucket = bucket_list[num]
        bucket.append(arr[i])
    for i in range(len(bucket_list)):
        bucket_list[i].sort()
    sort_arr = []
    for sub_list in bucket_list:
        for element in sub_list:
            sort_arr.append(element)
    return sort_arr


my_arr = list([4.12, 6.421, 0.0023, 3.0, 2.123, 8.122, 4.12, 10.09])
print(bucket_sort_v1(my_arr))
