#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   JZ4.reConstructBinaryTree.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/6/2 12:34 下午   Lita       1.0         None
"""

"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre and not tin:
            return None
        if len(pre) != len(tin):
            return None

        # 取出pre的值
        root = pre[0]
        rootNode = TreeNode(root)

        pos = tin.index(root)
        tinLeft = tin[:pos]
        tinRight = tin[pos+1:]

        preLeft = pre[:pos]




