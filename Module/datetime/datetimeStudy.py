#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   datetimeStudy.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/5/31 4:46 下午   Lita       1.0         None
"""

"""
Python 的datetime模块 其实就是date和time 模块的结合， 常见的属性方法都比较常用 
比如： 
datetime.day,datetime.month,datetime.year 分别表示一个datetime对象的日，月，年；如下
"""

from datetime import datetime

dt = datetime.now()  # 创建一个datetime类对象
print(dt.year, dt.month, dt.day)

"""
输出为：
2015 3 8
"""
