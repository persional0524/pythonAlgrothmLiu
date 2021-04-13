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


def count_sort_v2(arr=[]):
    # 1.得到数列最大值最小值，并算出差值d
    max_v = arr[0]
    min_v = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_v:
            max_v = arr[i]
            print("max_v=" + str(max_v))
        if arr[i] < min_v:
            min_v = arr[i]
            print("min_v=" + str(min_v))
    d = max_v - min_v
    # 2.创建统计数组并统计对应元素个数
    count_arr = [0] * (d + 1)
    for i in range(len(arr)):
        count_arr[arr[i] - min_v] += 1
        print(count_arr)
    print("#" * 37)
    # 3.统计数组的变形，后面的元素等于前面的元素之和
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
        print(count_arr)
    # 4.倒序遍历原始数列，从统计数组中找到正确的位置，输出到结果数组
    sort_arr = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        sort_arr[count_arr[arr[i] - min_v] - 1] = arr[i]
        count_arr[arr[i] - min_v] -= 1
    return sort_arr


mylist = list([95, 94, 91, 98, 99, 90, 99, 93, 91, 92])

# count_sort_v1(mylist)
# count_sort_v2(mylist)
# print(count_sort_v1(mylist))
print(count_sort_v2(mylist))
