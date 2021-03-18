#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   coutSort.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/18 9:13 上午   Lita       1.0         None
"""


def count_sort_v1(arr=[]):
    # 1.找到最大值
    max_v = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_v:
            max_v = arr[i]
            print(max_v)
    # 2.根据数列最大值统计数组的长度
    count_arr = [0] * (max_v + 1)
    # 3.填充统计数组。遍历数列
    for i in range(0, len(arr)):
        count_arr[arr[i]] += 1
        print(count_arr)
    # 4.遍历统计数组，输出最终结果
    sort_arr = []
    for i in range(0, len(count_arr)):
        for j in range(0, count_arr[i]):
            sort_arr.append(i)
    return sort_arr


mylist = list([4, 4, 6, 5, 3, 2, 8, 1, 7, 5, 6, 0, 10, 11, 23])

#count_sort_v1(mylist)
print(count_sort_v1(mylist))
