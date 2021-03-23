#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   MatplotlibP3.py
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/23 12:08 下午   Lita       1.0         None
"""

import matplotlib.pyplot as plt

"""
饼图：用于表示不同分类的占比情况，通过弧度大小来对比各类数据。
特点：分类数据的占比情况统计（分类）
"""
# 饼图
labels_value = ['walking', 'driving', 'sleeping', 'relaxing']
slices = [2, 1, 7, 14]
colors_value = ['r', 'y', 'g', 'b']
plt.pie(slices, labels=labels_value, autopct='%.2f', colors=colors_value, shadow=True, explode=(0, 0.1, 0, 0))
plt.title("Pie Graph")
plt.savefig('Pie.jpg')
plt.show()
