#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   JZ2.replaceSpace.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/5/17 8:43 下午   Lita       1.0         None
"""


class Solution:
    def replaceSpace_v1(self, s):
        # write code here
        li = []
        for i in range(len(s)):
            # print(i)
            if s[i] == ' ':
                li.append("%")
                li.append("2")
                li.append("0")
            else:
                li.append(s[i])
        return "".join(li)

    def replaceSpace_v2(self, s):
        l = []
        for i in s:
            if i == ' ':
                l.append('%20')
            else:
                l.append(i)
        return ''.join(l)

    def replaceSpace_v3(self, s):
        a = ""
        for i in s:
            if i == " ":
                a += "%20"
            else:
                a += i
        return a


if __name__ == '__main__':
    s = Solution()
    print(s.replaceSpace_v1("We Are Happy"))
    print(s.replaceSpace_v2("We Are Happy"))
    print(s.replaceSpace_v3("We Are Happy"))
