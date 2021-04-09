#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   mergeSort.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/30 10:16 下午   Lita       1.0         None
"""

"""
  [2,5,7,8,9]|[1,3,4,6] --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
  1、两个有序的列表合成一个有序的列表。--一次归并



"""


def merge(li, low, mid, high):  # 一次归并，面试必问(前提，都有序)
    # 列表有两段有序：[low,mid] [mid + 1,high],已排序
    i = low
    j = mid + 1
    li_tmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            li_tmp.append(li[i])
            i += 1
        else:
            li_tmp.append(li[j])
            j += 1
    while i <= mid:
        li_tmp.append(li[i])
        i += 1
    while j <= mid:
        li_tmp.append(li[j])
        j += 1
    # 左闭右开
    # way 1
    # j = 0
    # for i in range(low,high+1):
    #     li[i] = li_tmp[j]
    #     j += 1
    # way 2 li_tmp[0:high-low+1] li[low:high+1]
    for i in range(low, high + 1):
        li[i] = li_tmp[i - low]
    # way 3 切片可以直接赋值
    # li[low:high+1] = li_tmp


li = [2, 5, 7, 8, 9, 1, 3, 4, 6]
merge(li, 0, 4, 8)
print(li)
