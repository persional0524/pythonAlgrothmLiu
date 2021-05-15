#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   2340.lower.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/5/15 4:09 下午   Lita       1.0         None
"""

### s = 'AAA'

def count_upper_and_lower(s):
    li=list(s)
    j = 0
    for i in li:
        #print(i)
        if i.islower():
            j +=1
    print(j)


s = input()
count_upper_and_lower(s)