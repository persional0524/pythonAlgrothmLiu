#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   JZ.8jumpFloor.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/5/17 12:54 下午   Lita       1.0         None
"""

class Solution:
    def jumpFloor_v1(self, number):
        # write code here
        if number <= 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        a = 1
        b = 2
        cnt = 0
        i = 3
        while i <= number:
            cnt = a + b
            a = b
            b = cnt
            i += 1
        return cnt


    def jumpFloor_v2(self, number):
        if number <= 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        a = 2
        b = 1
        cnt = 0
        for i in range(3, number + 1):
            cnt = a + b
            b = a
            a = cnt
        return cnt

if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloor_v1(10))
    print(s.jumpFloor_v2(10))