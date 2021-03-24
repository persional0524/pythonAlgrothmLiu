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
import numpy
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
    #result = car[(car['厂商'] == '北京奔驰') & (car['销售月份'] == '201901')][['车型', '销量']]
    result = car[(car['厂商'] == '北京奔驰') & (car['销售月份'] == 201901)][['车型', '销量']]
    print(result)
    plt.bar(result['车型'], result['销量'])
    plt.show()


#def export_exercise_v1(file):





series()
DDataF_v1()
DDataF_v2()

file_1 = "/Users/liutao/PycharmProjects/pythonAlgrothmLiu/DateFile/students_complete.csv"
file_2 = '/Users/liutao/PycharmProjects/pythonAlgrothmLiu/DateFile/热销乘用车销量数据2019.xls'
# DDataF_readCsv_v1(file_1)
# DDataF_readExecl_v1(file_2)
# DDataF_readExecl_v2(file_2)
# Data_filtrateCsv_v1(file_1)
# Data_filtrateCsv_v2(file_1)
# total_v1(file_1)
exercise_v1(file_2)
