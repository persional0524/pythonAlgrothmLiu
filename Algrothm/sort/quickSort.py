#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   quickSort.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/24 9:14 下午   Lita       1.0         None
"""


def quick_sort_v1(start_v, end_v, arr=[]):
    #
    if start_v >= end_v:
        return

    mid = partition_v1(start_v, end_v, arr)
    quick_sort_v1(start_v, mid - 1, arr)
    quick_sort_v1(mid + 1, end_v, arr)


def partition_v1(start_v, end_v, arr=[]):
    left = 0
    right = end_v
    pivot = arr[start_v]

    while left != right:
        while left < right and arr[right] > pivot:
            right -= 1
        while left < right and arr[left] <= pivot:
            left += 1
        if left < right:
            tmp = arr[left]
            arr[left] = arr[right]
            arr[right] = tmp
    arr[start_v] = arr[left]
    arr[left] = pivot
    return left


my_arr = list([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
quick_sort_v1(0, len(my_arr) - 1, my_arr)
print(my_arr)
