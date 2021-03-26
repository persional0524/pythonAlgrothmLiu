#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   test.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/22 12:58 下午   Lita       1.0         None
"""
import pandas as pd
from matplotlib import pyplot as plt

print("hello")
print(22 % 3)


def cylinder_v(height, radius):
    pi = 3.14
    return pi * radius ** 2 * height


# print(cylinder_v(10, 20))
# print(cylinder_v(1000, 903))
# print(cylinder_v(88, 22))
# print(cylinder_v(90, 234))

def series():
    """
    1 带标签的数组
    2 一维数据，标签
    3 统计方法
    :return:
    """
    s = pd.Series([98, 92, 73, 64, 95], index=['小红', '小刚', '小强', '小丽', '小军'])
    print(s)
    print(s['小强'])
    #
    print(s.mean())
    print(s.max())


def DDataF_v1():
    dict_date = [{'name': 'Alex', 'age': '12'},
                 {'name': 'Bob', 'age': '15'},
                 {'name': 'Jack', 'age': '18'}]
    df = pd.DataFrame(dict_date)
    print(df)


def DDataF_v2():
    date = [['Alex', 12], ['Bob', 13]]
    # index:行标识
    students = pd.DataFrame(date, index=['202101', '202102'],
                            columns=['name', 'age'])
    print(students)
    print(students.loc['202101'])


def DDataF_readCsv_v1(file):
    student = pd.read_csv(file, header=0)
    print(student.head(10))


def DDataF_readExecl_v1(file):
    car = pd.read_excel(file)
    print(car.head(10))


def DDataF_readExecl_v2(file):
    car = pd.read_excel(file, sheet_name='市场影响力')
    print(car.head(10))


def Data_filtrateCsv_v1(file):
    student = pd.read_csv(file, header=0)
    print(student.head(10))
    print(student['student_name'])
    print(student[['student_name', 'reading_score', 'math_score']])


def Data_filtrateCsv_v2(file):
    student = pd.read_csv(file, header=0, index_col='Student ID')
    print(student.head(10))
    # loc=location 第5行
    print(student.loc[5])
    #
    print(student.loc[[1, 3, 5]])
    # loc=location 第5-9行,不是左闭右开，是左闭右闭
    print(student.loc[5:9])
    print(student.loc[5:9][['student_name', 'reading_score']])
    print(type(student.loc[5:9]))

    print(student[student['math_score'] > 90])
    print(student[(student['math_score'] > 90) & (student['reading_score'] > 90)])
    print(student[(student['math_score'] > 90) | (student['reading_score'] > 90)])
    print(student[(student['math_score'] > 90) & (~(student['reading_score'] > 90))])


def total_v1(file):
    student = pd.read_csv(file, header=0, index_col='Student ID')
    """
    d1.count()         #非空元素计算
    d1.min()           #最小值
    d1.max()           #最大值
    d1.idxmax()        #最大值的位置
    d1.idxmin()        #最小值的位置
    d1.quantile(0.1)   #10%分位数
    d1.sum()           #10%分位数
    d1.mean()          #均值
    d1.median()        #中位数
    d1.mode()          #众数
    d1.var()           #方差
    d1.nunique()          #去重
    
    
    """
    print(student[['reading_score', 'math_score']].mean())
    print(student[['reading_score', 'math_score']].max())


def exercise_v1(file):
    car = pd.read_excel(file, header=0, sheet_name='销售数据')
    print(car)
    result = car[(car['厂商'] == '北京奔驰') & (car['销售月份'] == 201901)][['车型', '销量']]
    print(result)
    plt.bar(result['车型'], result['销量'])
    plt.show()


def groupBy_count_v1():
    class1_stuents = pd.DataFrame([[1, 'James', 'male', 99, 100, 85],
                                   [2, 'Betty', 'female', 99, 87, 85],
                                   [3, 'Jack', 'male', 100, 87, 85],
                                   [4, 'Lily', 'female', 82, 87, 85],
                                   [5, 'Bill', 'male', 88, 87, 85]],
                                  columns=['id', 'name', 'gender', 'math', 'english', 'chinese']
                                  )

    print(class1_stuents)
    student_group = class1_stuents.groupby('gender')
    for i in student_group:
        print('i=' + str(i))
    print(class1_stuents.groupby('gender').agg('mean'))
    print(class1_stuents.groupby('gender').mean)


def export_exercise_v1(file):
    class1_stuents = pd.DataFrame([[1, 'James', 'male', 99, 100, 85],
                                   [2, 'Betty', 'female', 99, 87, 85],
                                   [3, 'Jack', 'male', 100, 87, 85],
                                   [4, 'Lily', 'female', 82, 87, 85],
                                   [5, 'Bill', 'male', 88, 87, 85]],
                                  columns=['id', 'name', 'gender', 'math', 'english', 'chinese']
                                  )

    print(class1_stuents)
    class1_stuents.to_csv('/Users/liutao/PycharmProjects/pythonAlgrothmLiu/DateFile/students_data.csv', index=False)


def Data_filtrate_sort_v1():
    class1_stuents = pd.DataFrame([[1, 'James', 'male', 99, 100, 85],
                                   [2, 'Betty', 'female', 99, 87, 85],
                                   [3, 'Jack', 'male', 100, 87, 85],
                                   [4, 'Lily', 'female', 82, 87, 85],
                                   [5, 'Bill', 'male', 88, 87, 85]],
                                  columns=['id', 'name', 'gender', 'math', 'english', 'chinese']
                                  )
    # 数学从大到小，英语从小到大
    sort_result = class1_stuents.sort_values(by=['math', 'english'], ascending=[False, True])
    print(sort_result)


def TaBao_pv_count_v1(file):
    taobao_date = pd.read_csv(file, header=0)
    print(taobao_date.head(10))
    # behavior_type 1:浏览 2:购物车 3:收藏 4:购买
    # PV page view，每一天的用户访问量
    pv_daily = taobao_date[['date', 'user_id']].groupby('date').agg('count')
    # print(pv_daily)
    plt.plot(pv_daily.index, pv_daily['user_id'])
    plt.xticks(rotation=45)
    plt.show()


def TaBao_pv_count_v2(file):
    taobao_date = pd.read_csv(file, header=0)
    print(taobao_date.head(10))
    # behavior_type 1:浏览 2:购物车 3:收藏 4:购买

    # 一天中，不同时间段，用户行为的数量
    pv_daily = taobao_date[['hour', 'user_id']].groupby('hour').agg('count')
    print(pv_daily)
    plt.plot(pv_daily.index, pv_daily['user_id'])
    plt.xticks(rotation=45)
    plt.show()


def TaBao_pv_count_v3(file):
    taobao_data = pd.read_csv(file, header=0)
    print(taobao_data.head(10))
    # behavior_type 1:浏览 2:购物车 3:收藏 4:购买
    """
    用户买东西
    （1）浏览
    （2）加入购物车或者收藏
    （3）购买
    了解用户的流失情况
    不同行为都有多少条
    """
    behavior_data = taobao_data[['behavior_type', 'user_id']].groupby('behavior_type').agg('count')
    print(behavior_data)
    view = behavior_data.loc[1]['user_id']
    print(view)
    cart = behavior_data.loc[2]['user_id']
    collect = behavior_data.loc[3]['user_id']
    buy = behavior_data.loc[4]['user_id']

    view_to_car = (cart + collect) / view
    cat_to_collect = buy / (cart + collect)

    print("从浏览到加入购物车或者收藏的转化率")
    print(view_to_car)
    print("从购物车或者收藏到购买的转化率")
    print(cat_to_collect)


def TaBao_pv_count_v4(file):
    taobao_data = pd.read_csv(file, header=0)
    print(taobao_data.head(10))
    # behavior_type 1:浏览 2:购物车 3:收藏 4:购买
    """
    # 复购率    重复购买的人数/总人数
    # 不是一锤子买卖，一个月内用户重复进行了在淘宝的购物
    
    # 多少人购买，去重复
    # 是不是有多少组就有多少用户
    """
    total_user = len(taobao_data[taobao_data['behavior_type'] == 4].groupby('user_id')).agg('count')

    # 多少人复购，多少人重复购买东西，购买行为大于1次
    repeat_user = taobao_data[taobao_data['behavior_type'] == 4][['user_id', 'item_id']].groupby('user_id').agg('count')
    repeat_user_num = len(repeat_user[repeat_user['item_id'] > 1])
    print(repeat_user)
    print(repeat_user_num)

    # 复购率
    ratio = repeat_user_num / total_user
    print("复购率 ： " + ratio)

series()
DDataF_v1()
DDataF_v2()

file_1 = "/Users/liutao/PycharmProjects/pythonAlgrothmLiu/DateFile/students_complete.csv"
file_2 = '/Users/liutao/PycharmProjects/pythonAlgrothmLiu/DateFile/热销乘用车销量数据2019.xls'
file_3 = '/Users/liutao/Downloads/taobao_data.csv'
# DDataF_readCsv_v1(file_1)
# DDataF_readExecl_v1(file_2)
# DDataF_readExecl_v2(file_2)
# Data_filtrateCsv_v1(file_1)
# Data_filtrateCsv_v2(file_1)
# total_v1(file_1)
# exercise_v1(file_2)
# groupBy_count_v1()
# export_exercise_v1(file_1)
# Data_filtrate_sort_v1()
# TaBao_pv_count_v1(file_3)
# TaBao_pv_count_v2(file_3)
# TaBao_pv_count_v3(file_3)
TaBao_pv_count_v4(file_3)
