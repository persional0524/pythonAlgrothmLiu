#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   MatplotlibP5.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/23 11:48 下午   Lita       1.0         None
"""

"""
1.使用两个条形图叠加覆盖来实现。
2.漏斗图一般都是从开始环节到结束环节层层递减的，
第一个环节的条形图长度就是自身的数据，
第二个环节的长度是自身的数据加上第一环节和当前环节的差的一半。
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import (TextArea,AnnotationBbox)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文乱码
N = 3  # N个环节
HEIGHT = 0.55  # 条形图的每个方框的高度
x1 = np.array([100, 50, 30])  # 各环节的数据
x2 = np.array((x1.max() - x1) / 2)  # 占位数据
x3 = []  # 画图时的条形图的数据
for i, j in zip(x1, x2):
    x3.append(i + j)
x3 = np.array(x3)
y = np.arange(N)[::-1]  # 倒转y轴。
labels = ['注册', '留存', '付费']  # 各个环节的标签。

# 画板和画纸
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)

# 绘图
ax.barh(y, x3, HEIGHT, tick_label=labels, color='blue', alpha=0.85)  # 主条形图
ax.barh(y, x2, HEIGHT, color='white', alpha=1)  # 覆盖主条形图的辅助数据
# 转化率
rate = []
for i in range(len(x1)):
    if i < len(x1) - 1:
        rate.append('%2.2f%%' % ((x1[i + 1] / x1[i]) * 100))  # 转化率的横坐标。
y_rate = [(x1.max() / 2, i - 1) for i in range(len(rate), 0, -1)]  # 转化率

# 标注转化率
for a, b in zip(rate, y_rate):
    offsetbox = TextArea(a, minimumdescent=False)
    ab = AnnotationBbox(offsetbox, b,
                        xybox=(0, 40),
                        boxcoords="offset points",
                        arrowprops=dict(arrowstyle="->"))
    ax.add_artist(ab)

# 设置x轴y轴标签
ax.set_xticks([0, 100])
ax.set_yticks(y)

# 显示图形
plt.show()
