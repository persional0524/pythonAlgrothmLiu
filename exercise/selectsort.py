#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   selectsort.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/1 11:15 下午   Lita       1.0         None
"""


# def select_sort(arr=[]):
#     for i in range(len(arr)):
#         min = arr[0]
#         for j in range(i+1, len(arr)):
#             if arr[j] < min:
#                 tmp = arr[j]


def showdata(data):
    for i in range(8):
        print("%3d" % data[i], end="")
    print()


def select(data):
    for i in range(7):
        for j in range(i + 1, 8):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
    print()


data = [16, 25, 39, 27, 12, 8, 45, 63]
print("原始值：")
for i in range(8):
    print("%3d" % data[i], end="")
print("\n---------------------------------------")
select(data)
print("排序后的数据：")
for i in range(8):
    print("%3d" % data[i], end="")
print("")
