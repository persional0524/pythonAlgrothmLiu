#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   mySqrt.py
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/13 21:19 下午   Lita     1.0         None
"""
import pandas as pd
from pandas import DataFrame
#读
#r'C:\Users\HUAWEI\Desktop\example.xlsx'
file = '/Users/liutao/Desktop/360工作/账单/202102/新沂聚爱202102付款通知.xlsx'
data = pd.read_excel(file,engine='openpyxl',sheet_name='社保明细',header = None,skiprows= 4,usecols=[1, 2])
eData=data.fillna(method='ffill')

out_path = '/Users/liutao/Desktop/360工作/账单/202102/新沂聚爱202102付款通知-Exchange.xlsx'
out_write = pd.ExcelWriter(out_path)
#查看所有的值
#print(eData.values)
disName = eData.drop_duplicates(2)
print(disName)
#查看第一行的值
#print(data.valus[0])

#print(eData.columns)

for id in disName.itertuples():
    print(id[0],id[1],id[2])

dict1 = {'所属公司'}

disName.to_excel(out_write,'数据整合')
out_write.save()

