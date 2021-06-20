#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   Offer11.minArray.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/6/17 2:49 下午   Lita       1.0         None
"""


class Solution:
    def minArray_v1(self, numbers):
        n = len(numbers)
        if n <= 0:
            return None
        i, j = 0, len(numbers) - 1
        while i <= j:
            m = (i + j) >> 1
            if numbers[m] > numbers[j]:
                i = m + 1
            elif numbers[m] < numbers[j]:
                j = m
            else:
                # j -= 1
                return min(numbers[i:j])
        # 对于寻找此类数组的最小值问题，可直接放弃二分查找，而使用线性查找替代
        return numbers[i]


if __name__ == '__main__':
    s = Solution()
    print(s.minArray_v1([3, 4, 5, 1, 2]))
    print(s.minArray_v1([2, 2, 2, 0, 1]))
