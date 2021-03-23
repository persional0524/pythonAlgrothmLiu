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

底层的容器层：主要包括Canvas(画板)、Figure(画布、图片)、Axes(图表)； 一个axes代表一个图表，包含一个plot，一个figure代表一张画布绘制一张图片，一张图片或一张画布可以有多个图表；
canvas画板，摆放画布的工具。关系：画板--->画布或图片-->线条、饼图等图片
辅助显示层：主要包括Axis坐标轴、Spines、Tick、Grid、Legend、Title等，该层可通过set_axis_off()或set_frame_on(False)等方法设置不显示；
图像层：即通过plot、contour、scatter等方法绘制的图像。


"""
# 散点图（x，y）
x = [1, 2, 3, 4, 5]
y = [2.3, 3.4, 1.2, 6.6, 7.8]

plt.scatter(x, y, edgecolors='red', marker="*", s=200, alpha=0.5)
plt.savefig('figure.jpg')
plt.show()
