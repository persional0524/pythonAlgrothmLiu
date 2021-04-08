#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   1.two_sum.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/7 3:06 下午   Lita       1.0         None
"""


def twosum_v1(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if target == arr[i] + arr[j]:
                return [i, j]
    return []

"""
复杂度分析

时间复杂度：O(N^2)
其中 N是数组中的元素数量。最坏情况下数组中任意两个数都要被匹配一次。

空间复杂度：O(1)。

"""


def twoSum_v2(nums, target):
    hashtable = dict()
    # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
    # Python 2.3. 以上版本可用，2.6 添加 start 参数。

    """
    参数
    sequence -- 一个序列、迭代器或其他支持迭代对象。
    start -- 下标起始位置。
    """
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i
    return []

"""
复杂度分析

时间复杂度：O(N)，其中 NN 是数组中的元素数量。对于每一个元素 x，我们可以 O(1) 地寻找 target - x。

空间复杂度：O(N)，其中 NN 是数组中的元素数量。主要为哈希表的开销。

"""


my_list = ([2, 15, 11, 7])
# print(twosum_v1(my_list, 9))
print(twoSum_v2(my_list, 9))