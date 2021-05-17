#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   JZ5.CQueue.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/5/17 10:25 下午   Lita       1.0         None
"""


class Soluation:
    def __init__(self):
        pass
        """
        栈A   栈B
        | |   | |
        |3|   |1|
        |2|   |2|
        |1|   |3|
        ***   ***

        1）进入队列：1，2，3
        2）弹出队列第一个元素：1
        3）弹出队列第二个元素：2
        4）进入队列：4，5，6
        5）弹出队列第一个元素：3
        ...
        
        
        解题思路：
        1）栈A存放进入队列的元素
        2）栈B存放即将弹出的元素：
           判断栈B是否为空，如果不为空，则弹出B最上面的元素
                         如果为空，则栈A中所有元素移到栈B中
           如果 栈A和栈B同时为空，则返回-1
        """

        self.stack_a = []
        self.stack_b = []

    def push(self, node):
        # write code here
        self.stack_a.append(node)

    def pop(self):
        # return xx
        if not self.stack_a and not self.stack_b:
            return -1

        if self.stack_b:
            return self.stack_b.pop(-1)

        while self.stack_a:
            self.stack_b.append(self.stack_a.pop(-1))

        return self.stack_b.pop(-1)
