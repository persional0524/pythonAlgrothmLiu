#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   bubblesort.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/5/22 9:45 上午   Lita       1.0         None
now fight
"""
import random



"""
[8, 17, 7, 12, 11, 6, 3, 16, 13, 5, 1, 9, 2, 14, 10, 15, 4, 0, 19, 18]
[19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
"""
def bubblesort_v1(li=[]):
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
           if li[j+1] < li[j]:
               li[j+1],li[j] = li[j],li[j+1]



def bubblesort_v2(li=[]):
    for i in range(len(li) - 1):
        is_sort = True
        for j in range(len(li) - i - 1):
           if li[j+1] < li[j]:
               li[j+1],li[j] = li[j],li[j+1]
               is_sort = False
        if is_sort:
            break


li = list(range(20))
random.shuffle(li)
print(li)
bubblesort_v2(li)
print(li)