#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   bubbleSort.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/12 10:32 下午   Liutaou      1.0         None
'''



def bubble_sort_v1(arr=[]):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp


def bubble_sort_v2(arr=[]):
    for i in range(len(arr) - 1):
        is_sort = True
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
                is_sort = False

        if is_sort:
            break


def bubble_sort_v3(arr=[]):
    for i in range(len(arr)):
        last_index = 0
        sort_border = len(arr) - 1
        is_sort = True
        for j in range(sort_border):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
                last_index = j
                is_sort = False

        sort_border = last_index
        if is_sort:
            break


mylist = [45, 4, 7, 44, 3, 7, 8, 2, 9, 13, 6, 10, 34]
bubble_sort_v3(mylist)
print(mylist)
