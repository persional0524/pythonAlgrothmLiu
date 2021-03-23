#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   MatplotlibP2.py
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/23 12:08 下午   Lita       1.0         None
"""

import matplotlib.pyplot as plt

# 折线图（x，y）
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [6, 9, 14, 21, 30, 41, 54, 69]
z = [55, 105, 155, 205, 305, 355, 405]

plt.plot(x, y)
plt.plot(x, z)
plt.xlabel('week')
plt.ylabel('stock')
plt.title('Stock Price')
plt.legend(['y = x**2 +5', 'z = x * 50 +5'])
plt.show()
