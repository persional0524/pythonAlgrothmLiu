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


# import lib

def binarySearch_v1(arr, target):
    if len(arr) == 0:
        return -1

    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return target
        elif target < arr[mid]:
            right == mid - 1
        else:
            left == mid + 1

    return -1


def binarySearch_v2(nums, target):
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
            print("target = "+str(target))
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1


# binarySearch_v1([0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 23], 6)
binarySearch_v2([0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 23], 6)
