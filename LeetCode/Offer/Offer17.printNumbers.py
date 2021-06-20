#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   Offer17.printNumbers.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/6/14 1:27 下午   Lita       1.0         None
"""

"""
剑指 Offer 17. 打印从1到最大的n位数
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]

说明：

用返回一个整数列表来代替打印
n 为正整数
"""


class Solution:
    def printNumbers_v1(self, n):
        res = []
        for i in range(1, 10 ** n):
            res.append(i)
        return res

    def printNumbers_v2(self, n):
        return list(range(1, 10 ** n))

    """
    题的主要考点是大数越界情况下的打印。需要解决以下三个问题：
    """

    def printNumbers_v3(self, n):
        pass

    def printNumbers_v4(self, n: int) -> [int]:
        def dfs(x):
            if x == n:  # 终止条件：已固定完所有位
                res.append(''.join(num))  # 拼接 num 并添加至 res 尾部
                return
            for i in range(10):  # 遍历 0 - 9
                num[x] = str(i)  # 固定第 x 位为 i
                dfs(x + 1)  # 开启固定第 x + 1 位

        num = ['0'] * n  # 起始数字定义为 n 个 0 组成的字符列表
        res = []  # 数字字符串列表
        dfs(0)  # 开启全排列递归
        return ','.join(res)  # 拼接所有数字字符串，使用逗号隔开，并返回

    def printNumbers_v5(self, n: int) -> [int]:
        def dfs(x):
            if x == n:
                s = ''.join(num[self.start:])
                if s != '0': res.append(s)
                if n - self.start == self.nine: self.start -= 1
                return
            for i in range(10):
                if i == 9: self.nine += 1
                num[x] = str(i)
                dfs(x + 1)
            self.nine -= 1

        num, res = ['0'] * n, []
        self.nine = 0
        self.start = n - 1
        dfs(0)
        return ','.join(res)

    def printNumbers_v6(self, n: int) -> [int]:
        def dfs(x):
            if x == n:
                s = ''.join(num[self.start:])
                if s != '0': res.append(int(s))
                if n - self.start == self.nine: self.start -= 1
                return
            for i in range(10):
                if i == 9: self.nine += 1
                num[x] = str(i)
                dfs(x + 1)
            self.nine -= 1

        num, res = ['0'] * n, []
        self.nine = 0
        self.start = n - 1
        dfs(0)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.printNumbers_v1(1))
    print(s.printNumbers_v2(1))
    print(s.printNumbers_v4(2))
    print(s.printNumbers_v5(2))
    print(s.printNumbers_v6(2))
