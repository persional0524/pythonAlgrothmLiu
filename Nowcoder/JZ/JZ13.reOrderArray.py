#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   JZ13.reOrderArray.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/5/18 9:52 上午   Lita       1.0         None
"""
import random


class Solution:
    def reOrderArray_v1(self, array):
        # write code here
        li = []
        for i in array:
            if (i & 1) != 0:
                li.append(i)
        for i in array:
            if (i & 1) == 0:
                li.append(i)
        return li

    def reOrderArray_v2(self, array):
        li = []
        for i in array:
            if i % 2 == 1:
                li.append(i)
        for i in array:
            if i % 2 == 0:
                li.append(i)
        return li


if __name__ == '__main__':
    s = Solution()
    li = list(range(20))
    random.shuffle(li)
    print(li)
    print(s.reOrderArray_v1(li))
    print(s.reOrderArray_v2(li))
