#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   connMysql.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/5/25 11:49 下午   Lita       1.0         None
"""
import pandas as pd
from sqlalchemy import create_engine

file = '/Users/liutao/Desktop/360工作/账单/202102/新沂聚爱202102付款通知.xlsx'
df = pd.read_excel(file, engine='openpyxl', sheet_name='社保明细', header=None, skiprows=4, usecols=[1, 2])
engine = create_engine("mysql+mysqlconnector://root:123@localhost:3306/jd", echo=False)
eData = df.fillna(method='ffill')
disName = eData.drop_duplicates(2)
print(disName)
disName.to_sql(name='paytopic', con=engine, if_exists='replace')
