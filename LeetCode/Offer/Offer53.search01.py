#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   Offer53.search01.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/6/10 2:56 下午   Lita       1.0         None
"""


class Solution:
    def search(self, nums, target):
        def finRightPos(x):
            left, right = 0, len(nums) -1
            mid = left + (right - left) // 2
            if nums[mid] <= x:
                left = mid + 1
            else:
                right = mid - 1
            return left

        return finRightPos(target) - finRightPos(target - 1)

    def search_v1(self, nums, target):
        pass

    def search_v2(self, nums, target):
        def helper(tar):
            i, j = 0, len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                if nums[m] <= tar:
                    i = m + 1
                else:
                    j = m - 1
            return i

        return helper(target) - helper(target - 1)


if __name__ == '__main__':
    nums = list([5, 7, 7, 8, 8, 10])
    s = Solution()
    print(s.search(nums, 8))
    print(s.search_v2(nums, 8))
