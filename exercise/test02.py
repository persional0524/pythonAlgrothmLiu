#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   test02.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/29 10:16 上午   Lita       1.0         None
"""
import numpy as np

a = np.repeat(np.arange(5).reshape([1, -1]), 10, axis=0) + 10.0
b = np.random.randint(5, size=a.shape)
c = np.argmin(a * b, axis=1)
b = np.zeros(a.shape)
b[np.arange(b.shape[0]), c] = 1
print(b)

print("##" * 30)
# 生成数组[0,1,2,3,4]
a1 = np.arange(5)
print("#%s#" % ("a1"))
print(a1)
# 原数组共有x个元素，reshape([n,-1])意思是将原数组重组为n行x/n列的新数组
# 所以数组共有5个元素，重组为1行5列的数组
a2 = a1.reshape([1, -1])
print("#%s#" % ("a2"))
print(a2)
# 因为axis=0，所以是沿着横轴方向重复，增加行数
# 所以原数组增加10行
a3 = np.repeat(np.arange(5).reshape([1, -1]), 10, axis=0)
print("#%s#" % ("a3"))
print(a3)
# 数组每个元素都+10
a4 = np.repeat(np.arange(5).reshape([1, -1]), 10, axis=0) + 10
print("#%s#" % ("a4"))
print(a4)

# 随机生成大小为a.shape的数组，数组元素为[0,5)区间范围的整数。
b = np.random.randint(5, size=a.shape)
print("#%s#" % ("b"))
print(b)

# a*b组成的新数组，给出每行最小值的下标。
c = np.argmin(a * b, axis=1)
print("#%s#" % ("c"))
print(c)

# 生成a.shape大小的全零数组。
b = np.zeros(a.shape)
print("#%s#" % ("b"))
print(b)


"""
b.shape[0]表示b的行数，10行
b[np.arange(10), c]=1表示np.arange(10)生成的数组中，所有c对应的位置全置为1。
"""
b[np.arange(b.shape[0]), c] = 1
print("#%s#" % ("b"))
print(b)