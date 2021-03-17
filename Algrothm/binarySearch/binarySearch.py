#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""

@File    :   binarySearch.py
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/15 12:25 下午   Lita      1.0         None
"""

"""
模版-1
初始条件：left = 0, right = length-1
终止：left > right
向左查找：right = mid-1
向右查找：left = mid+1
"""


def binarySearch_v1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            print("target = " + str(target))
            print("mid = " + str(mid))
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1


"""
模版-2
初始条件：left = 0, right = length-1
终止：left > right
向左查找：right = mid
向右查找：left = mid+1

一种实现二分查找的高级方法。
查找条件需要访问元素的直接右邻居。
使用元素的右邻居来确定是否满足条件，并决定是向左还是向右。
保证查找空间在每一步中至少有 2 个元素。
需要进行后处理。 当你剩下 1 个元素时，循环 / 递归结束。 需要评估剩余元素是否符合条件。
"""


def binarySearch_v2(nums, target):
    if len(nums) == 0:
        return -1
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    if left != len(nums) and nums[left] == target:
        return left
    return -1


"""
模版-3

"""

binarySearch_v1([0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 23], 6)
print(binarySearch_v2([0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 23], 6))
