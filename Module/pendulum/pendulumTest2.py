#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   pendulumTest2.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/6/9 4:32 下午   Lita       1.0         None
"""
import pendulum

# 1、获取本周的周一和周日
now = pendulum.now()
print(now.to_date_string())
# 2021-01-14

print(now.start_of("week").to_date_string())
# 2021-01-11

print(now.end_of("week").to_date_string())
# 2021-01-17
