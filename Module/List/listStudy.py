#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   listStudy.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/10 3:54 下午   Lita       1.0         None
"""

"""
对任何范围[start:end],我们可以访问到包括 start 在内到 end(不包括 end)的所有字符，
换句话说，假设 x 是[start:end]中的一个索引值，那么有: start<= x < end
"""

aString = 'abcd'

print("aString的长度=" + str(len(aString)))
# 正向索引：索引值开始于 0,结束于总长度减 1(因为我们是从 0 开始索引的).
final_index = len(aString) - 1
print("aString的索引长度=" + str(final_index))
aString[0]
print("aString的第一个元素=" + str(aString[0]))
aString[1:3]
print("aString的值1=" + str(aString[1:3]))
# 左闭右开
aString[2:4]
print("aString的值2=" + str(aString[2:4]))
# aString[4]
# IndexError: string index out of range
# print("aString的值2="+str(aString[4]))
# 反向索引：在进行反向索引操作时,是从-1 开始，向字符串的开始方向计数，到字符串长度的负数为索引的结束,
final_index_r = -len(aString)
print("aString的长度=" + str(final_index_r))

aString[-1]
print("aString的第后一个元素=" + str(aString[-1]))

# 左闭右开
aString[-3:-1]
print("aString的倒数第3个元素和倒数第二个元素=" + str(aString[-3:-1]))
# 反向索引：在进行反向索引操作时,是从-1 开始
aString[-4]
print("aString的倒数第4个元素=" + str(aString[-4]))

"""
默认索引：如果开始索引或者结束索引没有被指定，则分别以字符串的第一个和最后一个索引值为默认值。
如果开始索引或者结束索引没有被指定，则分别以字符串的第一个和最后一个索引值为默认值。
"""
""">>> aString[2:]

'cd'

>>> aString[1:]

'bcd'

>>> aString[:-1]

'abc'

>>> aString[:]
'abcd'
"""
# 注意：起始/结束索引都没有指定的话会返回整个字符串.
