#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   insertSort.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/15 11:19 下午   Lita       1.0         None
"""


def insert_Sort_v1(arr=[]):
    for i in range(1, len(arr)):
        # 设置当前值的前一个元素的标识
        j = i - 1

        # 如果当前值小于前一个元素，将当前值作为一个临时变量存储，将前一个元素后移
        if arr[j] > arr[i]:
            tmp = arr[i]
            arr[j] = arr[i]

            # 继续往前寻找。如果有比临时变量值大的数字，则需要后移一位，直到找到比临时变量小的元素或者达到列表的第一个元素
            j = j - 1
            while j >= 0 and arr[j] > arr[i]:
                arr[j + 1] = arr[j]
                j = j - 1

            # 将临时变量赋值给合适的位置
            arr[j + 1] = tmp


mylist = list([4, 4, 6, 5, 3, 2, 8, 1, 7, 5, 6, 0, 10, 11, 23])

insert_Sort_v1(mylist)
print(mylist)
