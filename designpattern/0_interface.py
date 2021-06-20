#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   0_interface.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/6/2 11:10 上午   Lita       1.0         None
"""

# 接口作用，

from abc import ABCMeta, abstractmethod


# 抽象类-不能实例化的类
class Interface(metaclass=ABCMeta):
    @abstractmethod
    def func(self, arg):
        pass


class A(Interface):
    pass


# TypeError: Can't instantiate abstract class A with abstract methods func
a = A()


# 公用的，私有的在各自的类里面，这样写是有问题的
class User:
    pass


# 继承 User
class Student(User):
    pass


# 继承 User
class Teacher(User):
    pass


# 防傻子，程序这样一写，就有问题

# u = User  # User 对象是啥，啥也不是，防止这样，把User搞成抽象类，要么是Student类，要么是Teacher类

u = Student

# 函数签名：函数名，参数个数和类型