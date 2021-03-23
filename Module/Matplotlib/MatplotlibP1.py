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

"""
散点图：用两组数据构成多个坐标点，考察坐标点的分布，判断两变量之间是否存在某种关联或总结坐标点的分布模式。
特点：判断变量之间是否存在数量关联趋势，离群点（分布规律）
"""
# 散点图（x，y）
x = [1, 2, 3, 4, 5]
y = [2.3, 3.4, 1.2, 6.6, 7.8]

plt.scatter(x, y, edgecolors='red', marker="*", s=200, alpha=0.5)
plt.savefig('figure.jpg')
plt.show()
