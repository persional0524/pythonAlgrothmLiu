#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   MatplotlibP1.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/23 12:08 下午   Lita       1.0         None
"""

import matplotlib.pyplot as plt

# 散点图（x，y）
x = [1, 2, 3, 4, 5]
y = [2.3, 3.4, 1.2, 6.6, 7.8]

plt.scatter(x, y, edgecolors='red', marker="*", s=200, alpha=0.5)
plt.savefig('figure.jpg')
plt.show()
