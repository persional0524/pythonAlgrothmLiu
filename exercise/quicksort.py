#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   quicksort.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/31 8:47 下午   Lita       1.0         None
"""


def quick_sort(start, end, arr=[]):
    if start >= end:
        return
    # dg
    mid = partitons_v2(start, end, arr)
    #mid = partitons_v1(start, end, arr)
    quick_sort(start,mid - 1,arr)
    quick_sort(mid + 1,end,arr)


def partitons_v1(start, end, arr=[]):
    left = start
    right = end
    pivot = arr[start]
    while left != right:
        while left < right and arr[right] > pivot:
            right -= 1
        while left < right and arr[left] <= pivot:
            left += 1
        if left < right:
            tmp = arr[left]
            arr[left] = arr[right]
            arr[right] = tmp
    arr[start] = arr[left]
    arr[left] = pivot
    return left


def partitons_v2(start, end, arr=[]):
    pivot = arr[start]
    marks = start
    for i in range(start + 1,end + 1):
        if arr[i] < pivot:
            marks += 1
            tmp = arr[i]
            arr[i] = arr[marks]
            arr[marks] = tmp
    arr[start] = arr[marks]
    arr[marks] = pivot
    return marks


my_arr = list([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
quick_sort(0, len(my_arr) - 1, my_arr)
print(my_arr)
