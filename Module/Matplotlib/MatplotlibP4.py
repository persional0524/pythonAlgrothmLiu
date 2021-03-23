#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   MatplotlibP4.py.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/23 12:31 下午   Lita       1.0         None
"""

import matplotlib.pyplot as plt

"""
直方图：由一系列高度不等的纵向条纹或线段表示数据的分布情况。一般用横轴表示数据范围，纵轴表示分布情况。
特点：绘制连续性的数据展示一组或多组数据的分布状况（统计）
"""
# 直方图
plt.rcParams['font.sans-serif'] = ['SimHei']
x = ['北京', '上海', '深圳', '武汉', '沈阳']
y = [334, 60, 99, 100, 21]
plt.bar(x, y, color=['blue', 'red', 'green', 'yellow', 'black'])
plt.title("条形图")
plt.xticks(rotation=90)
plt.show()
