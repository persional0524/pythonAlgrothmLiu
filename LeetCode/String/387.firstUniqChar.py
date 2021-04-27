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
import collections

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


def firstUinqChar_v2(s):
    if len(s) == 1:
        return 0
    # 哈希算法，26个字母为键的字典
    words = [chr(i) for i in range(97, 126)]  # a-z
    values = [0] * 26
    wordDic = dict(zip(words, values))  # {'a':0,'b':0 ...}
    for word in s:
        wordDic[word] += 1
    for i in range(len(s)):
        if wordDic[s[i]] == 1:
            return i
    return -1


"""
方法3：使用哈希表存储频数
我们可以对字符串进行两次遍历。
在第一次遍历时，我们使用哈希映射统计出字符串中每个字符出现的次数。
在第二次遍历时，我们只要遍历到了一个只出现一次的字符，那么就返回它的索引，否则在遍历结束后返回 −1。

"""


def firstUinqChar_v3(s):
    # Counter({'h': 2, 'l': 2, 'e': 1, 'o': 1})
    frequency = collections.Counter(s)
    print(frequency)
    for i, ch in enumerate(s):
        print(i, ch)
        if frequency[ch] == 1:
            return i
    return -1


s = "aabbccd"
s1 = "leetcode"
s2 = "hhello"
print(firstUinqChar_v1(s))
print(firstUinqChar_v1(s1))
print(firstUinqChar_v3(s2))
