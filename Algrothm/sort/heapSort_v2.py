#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   heapSort_v2.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/5/11 5:45 下午   Lita       1.0         None
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = Heap(k + 1)
        for num in nums:
            if not heap.push(num):
                heap.pop()
                heap.push(num)
        if heap.size == k + 1:
            heap.pop()
        return heap.peek()


class Heap:
    def __init__(self, length):
        self.heap = [0] * (length + 1)
        self.size = 0

    def push(self, val):
        if self.size == len(self.heap) - 1:
            return False
        self.size += 1
        self.heap[self.size] = val
        self.shift_up(self.size)
        return True

    def pop(self):
        val = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap[self.size] = 0
        self.size -= 1
        self.shift_down(1)
        return val

    def peek(self):
        return self.heap[1]

    def shift_up(self, i):
        val = self.heap[i]
        while i >> 1 > 0:
            parent = i >> 1
            if val < self.heap[parent]:
                self.heap[i] = self.heap[parent]
                i = parent
            else:
                break
        self.heap[i] = val

    def shift_down(self, i):
        val = self.heap[i]
        while i << 1 <= self.size:
            child = i << 1
            if child != self.size and self.heap[child + 1] < self.heap[child]:
                child += 1
            if val > self.heap[child]:
                self.heap[i] = self.heap[child]
                i = child
            else:
                break
        self.heap[i] = val
