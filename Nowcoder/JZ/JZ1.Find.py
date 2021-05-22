#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   JZ1.Find.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/5/17 12:56 下午   Lita       1.0         None
"""


class Solution:
    # array 二维列表
    # 方法1：暴力法
    def Find_v1(self, target, array):
        # write code here
        for i in range(len(array)):
            for j in range(len(array[i])):
                if target == array[i][j]:
                    return True
        return False

    def Find_v2(self, target, array):
        # write code here
        for line in array:
            if target in line:
                return True
        return False

    # 二分查找
    def Find_v3(self, target, array):
        for i in range(len(array)):
            low = 0
            high = len(array[i]) - 1
            while low <= high:
                mid = low + ((high - low) >> 1)  # mid = low + (high - low) // 2
                if array[i][mid] == target:
                    return True
                if array[i][mid] < target:
                    low = mid + 1
                if array[i][mid] > target:
                    high = mid - 1
        return False

    def Find_v4(self, target, array):
        row_c = len(array)
        i = 0
        j = len(array[0]) - 1
        while i < row_c and j >= 0:
            value = array[i][j]
            if value == target:
                return True
            elif value > target:
                j -= 1
            else:
                i += 1
        return False

    def Find_v5(self, target, matrix):
        n = len(matrix)
        if n <= 0:
            return False
        m = len(matrix[0])
        i, j = 0, m - 1
        while i < n and j >= 0:
            value = matrix[i][j]
            if target == value:
                return True
            elif target > value:
                i += 1
            else:
                j -= 1
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.Find_v1(3, [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]))
    print(s.Find_v2(3, [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]))
    print(s.Find_v3(3, [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]))
    print(s.Find_v4(3, [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]))
    print(s.Find_v5(3, [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]))
