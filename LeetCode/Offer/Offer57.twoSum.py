#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   Offer57.twoSum.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/6/15 11:31 下午   Lita       1.0         None
"""


class Solution:
    def twoSum_v1(self, nums, target):
        dic = set()
        for n in nums:
            if target - n in dic:
                return n, target - n
            dic.add(n)
        return None

    def twoSum_v2(self, nums, target):
        i, j = 0, len(nums) - 1
        while i <= j:
            s = nums[i] + nums[j]
            if target == s:
                return nums[i], nums[j]
            elif target > s:
                i += 1
            else:
                j -= 1
        return None
