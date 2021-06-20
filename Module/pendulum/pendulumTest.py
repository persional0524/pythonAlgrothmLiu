#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   pendulumTest.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/6/9 4:29 下午   Lita       1.0         None
"""

import pendulum

# 1、获取时间
print(pendulum.now())
# 2019-12-12T15:52:35.837803+08:00

print(pendulum.today())
# 2019-12-12T00:00:00+08:00

print(pendulum.tomorrow())
# 2019-12-13T00:00:00+08:00

print(pendulum.yesterday())
# 2019-12-11T00:00:00+08:00


# 2、转字符串
print(pendulum.now().to_datetime_string())
# 2019-12-12 15:51:22

print(pendulum.now().to_date_string())
# 2019-12-12

print(pendulum.now().to_time_string())
# 22:25:05

print(pendulum.now().format('%Y-%m-%d'))
# 2019-12-12


# 3、类型测试
from datetime import datetime
dt =pendulum.datetime(2015, 2, 5)
print(isinstance(dt, datetime))
#True

print("####" * 30)

# 4、解析规范的时间
print(pendulum.from_format('2019-12-12', '%Y-%m-%d'))
# 2019-12-12T00:00:00+00:00

print(pendulum.parse('2019-12-12'))
# 2019-12-12T00:00:00+00:00


# 6、属性
now = pendulum.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
# 2019  12  12  22  22 45


# 7、时间加减
now = pendulum.now()
print(now)
# 2019-12-12T22:27:48.429761+08:00

print(now.add(years=1))
# 2020-12-12T22:27:48.429761+08:00

print(now.subtract(years=1))
# 2018-12-12T22:27:48.429761+08:00

# 时间跨度计算
print(now.diff(now.add(years=1)).in_years())
# 1


# 8、设置语言地区
pendulum.set_locale('zh')

print(pendulum.now().subtract(days=1).diff_for_humans())
# 1天前

print(pendulum.now().subtract(hours=1).diff_for_humans())
# 1小时前

# 9、生成时间序列
period = pendulum.period(pendulum.now(), pendulum.now().add(days=3))

# years, months, weeks, days, hours, minutes and seconds
for dt in period.range('days'):
    print(dt)

"""
2019-12-12T22:39:42.142193+08:00
2019-12-13T22:39:42.142193+08:00
2019-12-14T22:39:42.142193+08:00
2019-12-15T22:39:42.142193+08:00
"""

