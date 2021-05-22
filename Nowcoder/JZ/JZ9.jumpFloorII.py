#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   JZ9.jumpFloorII.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/5/17 12:55 下午   Lita       1.0         None
"""


class Solution:
    def jumpFloorII_v1(self, number):
        # write code here
        if number <= 2:
            return number
        res = [1, 2]
        for i in range(2, number):
            res.append(res[-1] * 2)
        return res[-1]

    def jumpFloorII_v2(self, number):
        if number <= 1:
            return 1
        cnt = 1
        a = 1
        for i in range(2, number + 1):
            cnt = 2 * a
            a = cnt
        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloorII_v1(10))
    print(s.jumpFloorII_v2(10))
