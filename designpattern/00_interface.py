#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   00_interface.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/6/2 9:50 下午   Lita       1.0         None
"""

from abc import abstractmethod, ABCMeta


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


# 实现接口

class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付%s元" % money)


class ApplePay(Payment):
    def pay(self, money):
        print("苹果支付%s元" % money)


class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%s元" % money)


p = ApplePay()
p.pay(100, 12)

# 函数签名: 函数名,参数个数和类型,返回值类型
