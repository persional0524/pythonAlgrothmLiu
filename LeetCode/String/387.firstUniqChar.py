#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   387.firstUniqChar.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/24 3:33 下午   Lita       1.0         None
"""

"""
387. 字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
"""


def firstUinqChar_v1(s):
    if len(s) == 1:
        return 0
    for i in range(len(s)):
        if s[i] not in s[i + 1:] and \
                s[i] not in s[:i]:
            return i
        return -1


s = "aabbccd"
print(firstUinqChar_v1(s))
