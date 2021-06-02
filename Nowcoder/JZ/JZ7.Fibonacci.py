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
        a = 1  # a 代表大数
        b = 0
        # n=4,循环3次
        for i in range(0, n - 1):
            # print("i="+str(i))
            cnt = a + b
            # print("cnt="+str(cnt))
            b = a
            a = cnt
        return cnt

    def Fibonacci_v3(self, n):
        res = [0, 1]
        i = 2
        while i <= n:
            res.append(res[i - 1] + res[i - 2])
            i = i + 1
        return res[n]

    def Fibonacci_v4(self, n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007
    """
    
    个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，
    但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。
    虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。
    看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。
    yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力，比起用类的实例保存状态来计算下一个 next() 的值，不仅代码简洁，而且执行流程异常清晰。
    """
    def fab(max):
        n, a, b = 0, 0, 1
        while n < max:
            yield b  # 使用 yield
            # print b
            a, b = b, a + b
            n = n + 1


if __name__ == '__main__':
    s = Solution()
    print(s.Fibonacci_v1(4))
    print(s.Fibonacci_v2(10))
    print(s.Fibonacci_v3(10))
    print(s.Fibonacci_v4(10))
    for n in s.fab(5):
        print(n)