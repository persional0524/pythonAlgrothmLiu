#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   Offer39.majorityElement.py.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/6/11 3:35 下午   Lita       1.0         None
"""

"""
本题常见的三种解法：
1.哈希表统计法:
2.数组排序法：
3.摩尔投票法：
"""


class Solution:
    def majorityElement_v1(self, nums):
        votes, count = 0, 0
        for num in nums:
            if votes == 0:
                x = num
            if num == x:
                votes += 1
            else:
                votes -= 1
        for num in nums:
            if num == x: count += 1
        return x if count > len(nums) >> 1 else 0


if __name__ == '__main__':
    nums = list([2, 3, 1, 0, 2, 5, 3])
    s = Solution()
    print(s.majorityElement_v1(nums))
