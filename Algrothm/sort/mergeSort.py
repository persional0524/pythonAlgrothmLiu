#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   mergeSort.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/30 10:16 下午   Lita       1.0         None
"""

"""
  [2,5,7,8,9]|[1,3,4,6] --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
  1、两个有序的列表合成一个有序的列表。--一次归并
  2、有了归并怎么用？
    时间复杂度：o(nlogn)
    空间复杂度：o(n)，开新列表了
  top:
        归并是先递归(merge_sort)，再执行的merge(一次归并)。
        快排是先执行mid(中间值)，再执行的递归(quick_sort)。
        
        先递归后打印，从小到大
        先打印后递归，从大到小
        排左边，排右边，合并一个列表

"""


# o(n)
def merge2list(li1, li2):
    i = 0
    j = 0
    li = []
    while i < len(li1) and j < len(li2):
        if li1[i] <= li2[j]:
            li.append(li1[i])
            i += 1
        else:
            li.append(li2[j])
            j += 1
    while i < len(li1):
        li.append(li1[i])
        i += 1
    while j < len(li2):
        li.append(li2[j])
        j += 1
    return li


# o(n)
def merge(li, low, mid, high):  # 一次归并，面试必问(前提，都有序)
    # 列表有两段有序：[low,mid] [mid + 1,high],已排序
    i = low
    j = mid + 1
    li_tmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            li_tmp.append(li[i])
            i += 1
        else:
            li_tmp.append(li[j])
            j += 1
    while i <= mid:
        li_tmp.append(li[i])
        i += 1
    while j <= high:
        li_tmp.append(li[j])
        j += 1
    # 左闭右开
    # way 1
    # j = 0
    # for i in range(low,high+1):
    #     li[i] = li_tmp[j]
    #     j += 1
    # way 2 li_tmp[0:high-low+1] li[low:high+1]
    for i in range(low, high + 1):
        li[i] = li_tmp[i - low]
    # way 3 切片可以直接赋值
    # li[low:high+1] = li_tmp


# o(logn)
def merge_sort(li, low, high):  # merge_sort：排序li的low到high的分为
    # if 长度 <2 什么都不做，长度< high 才开始做事情
    # low = high 一个元素，low > high 0个元素
    if low < high:
        mid = (low + high) // 2  # 分解 大-小 进去
        # print(li[low:mid+1],li[mid+1:high+1])
        # 递归 调用 merge_sort
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        print(li[low:mid + 1], li[mid + 1:high + 1])
        merge(li, low, mid, high)  # 合并 小-大 出来
        print("合并-排序=" + str(li[low:high + 1]))


# li1 = [2, 5, 7, 8, 9]
# li2 = [1, 3, 4, 6]
# print(merge2list(li1, li2))
#
# li = [2, 5, 7, 8, 9, 1, 3, 4, 6]
# merge(li, 0, 4, 8)
# print(li)
# print("#" * 30)

arr = [10, 4, 6, 3, 8, 2, 5, 7]
merge_sort(arr, 0, len(arr) - 1)
print(arr)
