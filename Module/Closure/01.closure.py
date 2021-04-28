#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   01.closure.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/28 10:41 上午   Lita       1.0         None
"""

"""
闭包：
    1、函数嵌套定义
        外部函数
            内部函数
                内部函数
    2、内部函数使用外部函数作用域的变量
    3、外部函数要有返回值，返回内部函数名

闭包要加装饰器，装饰器本身就是闭包。
"""


def func_out(func):
    # 写成通用的
    def func_in(*args, **kwargs):
        print("我是新增功能")
        return func(*args, **kwargs)

    return func_in


@func_out
# test = func_out(test)
def test():
    print("我是测试函数")


test()

###########################################

"""
闭包就是：
    1.一个函数（外函数）内部定义了一个函数（内函数）
    2.内函数调用了外函数的变量
    3.并且外函数的返回值是内函数的引用
    第一个adder5=adder（5）结束后，x=5，adder返回值为wrapper
    adder5(6)，此时wrapper(6)，所以值为11，x为5
    adder5(adder5(6))，同理，11+5=16
"""


def adder(x):
    def wrapper(y):
        return x + y

    return wrapper


adder5 = adder(5)
print(adder5(adder5(6)))
