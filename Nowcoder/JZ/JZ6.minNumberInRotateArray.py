#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   JZ6.minNumberInRotateArray.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/5/18 11:20 上午   Lita       1.0         None
"""

"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

示例1
输入

[3,4,5,1,2]
返回值

1

"""

# a = 10 # 1010
# for i in range(100):
#     print(i)
#     print("#=")
#     print(a << i)

# 位运算
def bin_m(n):
    if n > 0:
        return str(bin(n))[2:]
    else:
        return str(bin(n))[0] + str(bin(n))[3:]


print(bin_m(2222))
print(bin_m(-2222))
print("*"*50)
print('逻辑运算')

"""
基本类型转换bool的规律
数字0为假，非0为真
字符串空为假，其他为真
元组、列表、字典、集合空为假，只有有元素就为真

两个值相与，如果第一个值为真，那么返回第二个值；如果第一值为假，那么返回第一个值
两个值相或，如果第一个值为真，那么返回第一个值；如果第一值为假，那么返回第二个值

"""