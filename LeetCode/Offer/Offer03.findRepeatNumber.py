#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   Offer03.findRepeatNumber.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/6/10 10:05 上午   Lita       1.0         None
"""


class Solution:
    # 原地排序
    # O(N) ,O(1)
    def findRepeatNumber_v1(self, nums):
        for i, num in enumerate(nums):
            while nums[i] != i:
                m = nums[i]
                if nums[m] == m:
                    return m
                else:
                    nums[i] = nums[m]
                    nums[m] = m
        return -1

    # 哈希表
    # O(N) ,O(N)

    def findRepeatNumber_v2(self, nums):
        # set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
        dic = set()
        for num in nums:
            if num in dic: return num
            dic.add(num)
        return -1

    # 原地排序
    # O(N) ,O(1)
    def findRepeatNumber_v3(self, nums):
        i = 0
        while i <= len(nums):
            if nums[i] == i:
                i +=1
                continue
            if nums[nums[i]] == nums[i]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1


if __name__ == '__main__':
    nums = list([2, 3, 1, 0, 2, 5, 3])
    s = Solution()
    print(s.findRepeatNumber_v1(nums))
    print(s.findRepeatNumber_v2(nums))
    print(s.findRepeatNumber_v3(nums))