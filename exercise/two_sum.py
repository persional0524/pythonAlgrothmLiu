#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   two_sum.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/8 5:18 下午   Lita       1.0         None
"""


def two_sum_2(nums, target):
    hashtable = dict()
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i
    return []


nums = list([2, 3, 4, 5, 6, 7])
print(two_sum_2(nums, 6))
