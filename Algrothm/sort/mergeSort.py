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


def merge(li, low, mid, high):
    # 列表有两段有序：[low,mid] [mid + 1,high]
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
