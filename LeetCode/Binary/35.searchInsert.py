#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   35.searchInsert.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/6/23 11:14 下午   Lita       1.0         None
"""


class Solution:
    def searchInsert(self, nums, target):
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if target == nums[m]:
                return m
            elif target < nums[m]:
                j = m - 1
            else:
                i = m + 1
        return i


if __name__ == '__main__':
    nums = list([5, 7, 7, 8, 8, 10])
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 5))
    print(s.searchInsert([1, 3, 5, 6], 2))
    print(s.searchInsert([1, 3, 5, 6], 7))
    print(s.searchInsert([1, 3, 5, 6], 0))

