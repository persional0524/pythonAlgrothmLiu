#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   BinaryTreeTraversal.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/7 2:12 下午   Lita       1.0         None
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_binary_tree(input_list=[]):
    if input_list is None or len(input_list) == 0:
        return None

