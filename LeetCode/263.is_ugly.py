#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   263.is_ugly.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/10 1:32 下午   Lita       1.0         None
"""


def is_ugly_v1(nums):
    if nums <= 0:
        return False
    factors = [2, 3, 5]
    for factor in factors:
        print(factor)
        while nums % factor == 0:
            nums = nums // factor
            print(" "+str(nums))
    return nums == 1


print(is_ugly_v1(6))
print(is_ugly_v1(14))
