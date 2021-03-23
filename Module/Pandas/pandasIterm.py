#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   pandasIterm.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/12 11:36 下午   Lita      1.0         None
"""

import pandas as pd
from numpy import integer

"""
简单对上面三种方法进行说明：

iterrows(): 按行遍历，将DataFrame的每一行迭代为(index, Series)对，可以通过row[name]对元素进行访问。
itertuples(): 按行遍历，将DataFrame的每一行迭代为元祖，可以通过row[name]对元素进行访问，比iterrows()效率高。
iteritems():按列遍历，将DataFrame的每一列迭代为(列名, Series)对，可以通过row[index]对元素进行访问。
"""

inp = [{'c1':10, 'c2':100}, {'c1':11, 'c2':110}, {'c1':12, 'c2':123}]
df = pd.DataFrame(inp)

print(df)

print("[1] 按行遍历iterrows():")
for index, row in df.iterrows():
    print(index) # 输出每行的索引值

print("[1.1] 按行遍历iterrows():")
# 对于每一行，通过列名name访问对应的元素
for index,row in df.iterrows():
    print(row['c1'], row['c2']) # 输出每一行

print("[2] 按行遍历itertuples():")
for row in df.itertuples():
    print(getattr(row, 'c1'), getattr(row, 'c2')) # 输出每一行

print("[3] 按列遍历iteritems():")
for index, row in df.iteritems():

    print(index) # 输出列名
print("[3.1] 按列遍历iteritems():")
for index,row in df.iteritems():
    print(row[0], row[1], row[2]) # 输出各列




