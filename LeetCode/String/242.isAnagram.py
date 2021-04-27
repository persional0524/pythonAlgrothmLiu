#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   242.isAnagram.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/25 10:31 上午   Lita       1.0         None
"""

"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def isAnagram_v1(s, t):
    return sorted(list(s)) == sorted(list(t))


def isAnagram_v2(s, t):
    s_1 = list(s)
    s_1.sort()
    ss = "".join(s_1)
    t_1 = list(t)
    t_1.sort()
    tt = "".join(t_1)
    return ss == tt


s = "rat"
t = "car"

print(isAnagram_v1(s, t))
print(isAnagram_v2(s, t))
