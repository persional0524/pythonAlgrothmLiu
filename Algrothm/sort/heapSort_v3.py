#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   heapSort_v3.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/5/12 12:39 下午   Lita       1.0         None
"""
# -*- coding: utf-8 -*-

"""
堆
堆是一种完全二叉树， 有最大堆和最小堆特性
最大堆：父亲节点的值，大于孩子节点的值
最小堆：父亲节点的值，小于孩子节点的值

"""


class Array(object):
    def __init__(self, maxsize=32):
        self.maxsize = maxsize
        self._items = [None] * maxsize
        self.length = 0

    def __len__(self):
        return self.length

    def __setitem__(self, index, value):
        self._items[index] = value

    def __getitem__(self, index):
        return self._items[index]

    def clear(self):
        for i in range(len(self._items)):
            self._items[i] = None

    def __iter__(self):
        for item in self._items:
            yield item


###################################################
# 使用数组实现 最大堆
###################################################

class MaxHeap(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.array = Array(maxsize)
        self.len = 0

    def __len__(self):
        return self.len

    def add(self, value):
        """添加"""
        if self.len >= self.maxsize:
            raise Exception("Full Heap")
        self.array[self.len] = value
        self.len += 1
        self._siftup(self.len - 1)

    def _siftup(self, index):
        if index > 0:
            parent_index = int((index - 1) / 2)
            if self.array[index] > self.array[parent_index]:
                self.array[index], self.array[parent_index] = self.array[parent_index], self.array[index]
                self._siftup(parent_index)

    def extract(self):
        """删除根节点"""
        if self.len <= 0:
            raise Exception("Empty Heap")
        self.len -= 1
        value = self.array[0]
        self.array[0] = self.array[self.len]  # 将最后一个元素放在根节点
        self.array[self.len] = None  # 移除最后一位元素
        self._siftdown(0)
        return value

    def _siftdown(self, root_index):
        left = root_index * 2 + 1
        right = root_index * 2 + 2
        max_index = root_index
        if left < self.len and self.array[left] > self.array[max_index]:
            # 当right == self.len时表示无有孩子，不需要取比较值
            max_index = left
        if right < self.len and self.array[right] > self.array[max_index]:
            max_index = right
        if max_index != root_index:
            self.array[max_index], self.array[root_index] = self.array[root_index], self.array[max_index]
            self._siftdown(max_index)

    def remove(self, value):
        """删除堆中指定元素"""
        if self.len < 0:
            raise Exception("Empty Heap")
        index = self.get_index_with_value(value)
        if index == -1:
            raise Exception("No value")
        self.len -= 1
        self.array[index] = self.array[self.len]
        self.array = self.array[:self.len]
        self._siftdown(index)

    def get_index_with_value(self, value):
        index = 0
        for item in self.array:
            if item == value:
                return index
            index += 1
        return -1

    def heap_sort_reverse(self):
        """由大到小排序  删除了原有的堆 只返回来了元素"""
        heap_reverse_list = []
        for i in range(self.len):
            heap_reverse_list.append(self.extract())
        return heap_reverse_list

    ####################################################
    # 真正的堆排序 由大到小
    ####################################################
    def sort(self, to_sort_list):
        for num in to_sort_list:
            self.add(num)
        for last_index in range(self.len - 1, 0, -1):
            self.array[0], self.array[last_index] = self.array[last_index], self.array[0]
            self._re_heap(0, last_index)
        return list(self.array)

    def _re_heap(self, root_index, last_index):
        left = root_index * 2 + 1
        right = root_index * 2 + 2
        max_index = root_index
        if left < last_index and self.array[left] > self.array[max_index]:
            # 当right == self.len时表示无有孩子，不需要取比较值
            max_index = left
        if right < last_index and self.array[right] > self.array[max_index]:
            max_index = right
        if max_index != root_index:
            self.array[max_index], self.array[root_index] = self.array[root_index], self.array[max_index]
            self._re_heap(max_index, last_index)


def test_heap():
    heap = MaxHeap(9)
    nums = [12, 89, 33, 54, 78, 90, 23, 29, 40]
    for num in nums:
        heap.add(num)
    assert list(heap.array) == [90, 78, 89, 40, 54, 33, 23, 12, 29]

    heap.extract()
    assert list(heap.array) == [89, 78, 33, 40, 54, 29, 23, 12, None]

    heap.remove(78)
    assert list(heap.array) == [89, 54, 33, 40, 12, 29, 23]

    assert heap.heap_sort_reverse() == [89, 54, 40, 33, 29, 23, 12]

    to_sort_list = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    maxheap = MaxHeap(10)
    sorted_list = maxheap.sort(to_sort_list)
    print(sorted_list)
    assert sorted_list == [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]


###################################################
# 使用数组实现 最小堆
###################################################

class MinHeap(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self._len = 0
        self.array = Array(maxsize)

    def __len__(self):
        return self._len

    def add(self, value):
        if self._len >= self.maxsize:
            raise Exception("Full Heap")
        self.array[self._len] = value
        if self._len > 0:
            self._siftup(self._len)
        self._len += 1

    def _siftup(self, index):
        parent_index = int((index - 1) / 2)
        if parent_index >= 0:
            if self.array[index] < self.array[parent_index]:
                self.array[index], self.array[parent_index] = self.array[parent_index], self.array[index]
                self._siftup(parent_index)

    def extrace(self):
        """删除根节点  将最后一个元素放在根节点出 执行siftdown操作"""
        if self._len < 0:
            raise Exception("Empty Heap")
        self._len -= 1
        value = self.array[0]
        self.array[0] = self.array[self._len]
        self.array[self._len] = None
        self._siftdown(0)
        return value

    def _siftdown(self, root_index):
        min_index = root_index
        left = int(root_index * 2 + 1)
        right = int(root_index * 2 + 2)
        if left < self._len and self.array[left] < self.array[min_index]:
            min_index = left
        if right < self._len and self.array[right] < self.array[min_index]:
            min_index = right
        if root_index != min_index:
            self.array[root_index], self.array[min_index] = self.array[min_index], self.array[root_index]
            self._siftdown(min_index)

    def remove(self, value):
        if self._len <= 0:
            raise Exception("Empty Heap")
        index = self._find_index_with_value(value)
        if index == -1:
            raise Exception("No value")
        self._siftdown(index)
        self._len -= 1
        return value

    def _find_index_with_value(self, value):
        index = 0
        for i in range(self._len):
            if self.array[i] == value:
                return index
            index += 1
        return -1

    def heap_sort(self):
        """由小到大排序"""
        values = []
        for i in range(self._len):
            values.append(self.extrace())
        return values


def test_min_heap():
    ll = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    min_heap = MinHeap(9)
    for i in ll:
        min_heap.add(i)
    print(list(min_heap.array))
    assert list(min_heap.array)[:len(ll)] == [1, 2, 4, 3, 7, 8, 5, 9, 6]

    # 遍历伴随着删除，下面的单测会失败
    values = min_heap.heap_sort()
    ls = [i for i in range(1, 10)]
    assert values == ls

    # 删除操作
    for i in range(1, 10):
        root_value = min_heap.extrace()
        print(root_value)
        assert root_value == i

    import pytest
    with pytest.raises(Exception) as err_info:
        assert "Empty" in str(err_info.value)

    min_heap.add(10)
    assert min_heap.remove(10) == 10


###################################################
# 使用堆实现 优先级队列
# 思想：以元组的结构存储数据（priority，value），python比较tuple从第一个开始比较
###################################################

class PriorityQueue(object):
    def __init__(self, maxsize):
        self.heap = MaxHeap(maxsize)
        self.len = 0

    def push(self, value):
        self.heap.add(value)
        self.len += 1

    def pop(self, with_proprity=False):
        enter = self.heap.extract()
        self.len -= 1
        if with_proprity:
            return enter
        else:
            return enter[1]

    def traverse(self):
        return self.heap.array


def test_prioprity():
    a = [4, 6, 8, 3, 2, 9, 1]
    pq = PriorityQueue(32)
    for i in range(1, len(a) + 1):
        pq.push((i, a[i - 1]))
    assert list(pq.traverse())[:len(a)] == [(7, 1), (4, 3), (6, 9), (1, 4), (3, 8), (2, 6), (5, 2)]
    new_a = []
    for _ in range(pq.len):
        new_a.append(pq.pop(with_proprity=True)[1])
    assert new_a == a[::-1]


################################################
# top k 问题
################################################
def test_top():
    a = [4, 6, 8, 3, 2, 9, 1]
    heap = MaxHeap(32)
    for i in range(len(a)):
        heap.add(a[i])
    # 返回前4大元素
    tops = []
    for _ in range(4):
        tops.append(heap.extract())
    assert tops == [9, 8, 6, 4]