#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   02.classDecorators.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/28 11:02 上午   Lita       1.0         None
"""

"""
类装饰器
"""


class Test():
    def __init__(self, func):
        print("我是init方法")
        self.func = func
        print("我是新增功能")
        self.func()

    # TypeError: 'Test' object is not callable,--> 结局
    def __call__(self, *args, **kwargs):
        print("我是call方法")
        pass


@Test
# @Test == 【test = Test(test) 类装饰器】
def test():
    print("我是测试函数")


# test()

# 创建对象
# test = Test()
# TypeError: 'Test' object is not callable,对象是不能被调的
