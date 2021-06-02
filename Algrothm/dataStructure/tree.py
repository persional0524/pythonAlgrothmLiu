#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   tree.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/5/31 12:23 下午   Lita       1.0         None
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preOrderReducusive(root):
    if root == None:
        return None
    print(root.val)
    preOrderReducusive(root.left)
    preOrderReducusive(root.right)


def midOrderReducusive(root):
    if root == None:
        return None
    midOrderReducusive(root.left)
    print(root.val)
    midOrderReducusive(root.right)


def latOrderReducusive(root):
    if root == None:
        return None
    latOrderReducusive(root.left)
    latOrderReducusive(root.right)
    print(root.val)


# 非递归，栈-> 循环
def preOrder(root):
    if root == None:
        return None

    stack = []
    tmpNode = root
    while tmpNode or stack:
        while tmpNode:
            print(tmpNode.val)
            stack.append(tmpNode)
            tmpNode = tmpNode.left

        node = stack.pop()
        # print(node.val)     # 中序列遍历
        tmpNode = node.right  # 循环的下一个头
        # if node.right:
        #     stack.append(node.right)  # node.right 可能是空


# 栈弹出 ->中序遍历
def midOrder(root):
    if root == None:
        return None

    stack = []
    tmpNode = root
    while tmpNode or stack:
        while tmpNode:
            stack.append(tmpNode)
            tmpNode = tmpNode.left

        node = stack.pop()
        print(node.val)  # 中序列遍历
        tmpNode = node.right


def latOrder(root):
    if root == None:
        return None

    stack = []
    tmpNode = root
    while tmpNode or stack:
        while tmpNode:
            stack.append(tmpNode)
            tmpNode = tmpNode.left

        node = stack[-1]
        tmpNode = node.right
        if node.right == None:
            node = stack.pop()
            print(node.val)
            while stack and node == stack[-1].right:
                node = stack.pop()
                print(node.val)


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t8 = TreeNode(8)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    t6.right = t8

    # preOrderReducusive(t1)
    # print("*" * 30)
    # midOrderReducusive(t1)
    # print("*" * 30)
    # latOrderReducusive(t1)

    preOrder(t1)
    print("*" * 30)
    midOrder(t1)
    print("*" * 30)
    latOrder(t1)
