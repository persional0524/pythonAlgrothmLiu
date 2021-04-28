#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   test.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/28 12:30 下午   Lita       1.0         None
"""

"""

运行a[1::3]，从index=1开始，步
幅为3，到一个新的数组b，b=[2,5]；
"""
a = [1, 2, 3, 4, 5]

sums = sum(map(lambda x: x + 3, a[1::3]))
print(lambda x: x + 3, a[1::3])
print(sums)


