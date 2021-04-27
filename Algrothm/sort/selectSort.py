#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   selectSort.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/14 4:05 下午   Lita      1.0         None
"""


# import lib
def select_Sort_v1(arr=[]):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                tmp = arr[j]
                arr[j] = arr[min]
                arr[min] = tmp


def select_Sort_v2(arr=[]):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
                arr[i], arr[j] = arr[j], arr[i]


def select_Sort_v3(arr):
    if arr is not None:
        if arr == 1:
            pass
        else:
            for i in range(len(arr)):
                min = i
                for j in range(i + 1, len(arr)):
                    if arr[j] < arr[min]:
                        min = j
                        arr[i], arr[j] = arr[j], arr[i]


mylist = list([4, 4, 6, 5, 3, 2, 8, 1, 7, 5, 6, 0, 10, 11, 23])
select_Sort_v1(mylist)
# select_Sort_v2(mylist)
# select_Sort_v3(mylist)
print(mylist)
