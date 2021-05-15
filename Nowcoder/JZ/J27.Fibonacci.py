#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   J27.Fibonacci.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/5/15 5:18 下午   Lita       1.0         None
"""

"""
如果是按照递归来写的话，时间复杂度是随着n变化的。
增长率为 2^n
"""


class Solution:
    def Fibonacci_v1(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        # if n>1 f(n) = f(n-1) + f(fn-2)
        if n > 1:
            num = self.Fibonacci_v1(n - 1) + self.Fibonacci_v1(n - 2)
            return num

        return None

    """
    时间复杂度，2n---> o(n)
    """
    def Fibonacci_v2(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        a = 1 # a 代表大数
        b = 0
        # n=4,循环3次
        for i in range(0, n - 1):
            cnt = a + b
            b = a
            a = cnt
        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.Fibonacci_v1(4))
    print(s.Fibonacci_v2(10))