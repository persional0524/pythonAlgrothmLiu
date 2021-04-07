#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   heapSort.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/7 10:00 下午   Lita       1.0         None
"""


def sift(li, low, high):
    # li表示树，low表示树根， high表示最后一个节点的位置
    tmp = li[low]
    i = low
    j = 2 * i + 1  # 初始j指向空位的左孩子
    # i 指向空位，j指向两个孩子
    while j <= high:
        # 如果右孩子存在，且比左孩子大，指向右孩子
        if j + 1 <= high and li[j] < li[j+1]:
            j = j + 1
        if li[i] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1

