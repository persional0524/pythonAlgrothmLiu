#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   mySqrt.py
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/15 1:00 下午   Lita     1.0         None
"""

"""
实现"x的平方根"的两种方法

计算并返回x的平方根，x为非负整数
返回向下取整的整数(不包含小数点)
>>>
Input: 4
Output: 2
>>>
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""


def mySqrt_v1(target):  # 参数为目标的值，和下标没有什么太大关系

    """
    :param target:
    :rtype: int
    """

    left, right = 0, target
    mid = right // 2
    while left <= right:
        if mid * mid == target:
            return mid
        elif mid * mid > target:
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right) // 2
    return mid


def mySqrt_v2(target):
    return target ** 0.5


print(mySqrt_v1(16))
print(mySqrt_v2(16))
