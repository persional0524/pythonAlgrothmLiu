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
    # 递归条件结束
    if start_v >= end_v:
        return
    # 得到基准元素的位置
    # mid = partition_v1(start_v, end_v, arr)
    mid = partition_v2(start_v, end_v, arr)

    quick_sort_v1(start_v, mid - 1, arr)
    quick_sort_v1(mid + 1, end_v, arr)


def partition_v1(start_v, end_v, arr=[]):
    # 取第一个位置的匀速作为基准元素（也可以随机选取位置）
    left = start_v
    right = end_v
    pivot = arr[start_v]
    while left != right:
        # 控制right指针比较并且左移
        while left < right and arr[right] > pivot:
            right -= 1
        # 控制left指针比较并且右移动
        while left < right and arr[left] <= pivot:
            left += 1
        # 交换left和right的指向元素
        if left < right:
            tmp = arr[left]
            arr[left] = arr[right]
            arr[right] = tmp
    # pivot和指针重合点交换
    arr[start_v] = arr[left]
    arr[left] = pivot
    return left


def partition_v2(start_v, end_v, arr=[]):
    pivot = arr[start_v]
    marks = start_v
    for i in range(start_v + 1, end_v + 1):
        if arr[i] < pivot:
            marks += 1
            tmp = arr[marks]
            arr[marks] = arr[i]
            arr[i] = tmp
    arr[start_v] = arr[marks]
    arr[marks] = pivot
    return marks


my_arr = list([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
quick_sort_v1(0, len(my_arr) - 1, my_arr)
print(my_arr)
