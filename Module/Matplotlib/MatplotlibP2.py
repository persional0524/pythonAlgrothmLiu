#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   MatplotlibP2.py
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/23 12:08 下午   Lita       1.0         None
"""

from matplotlib import pyplot as plt
from matplotlib import font_manager
import numpy as np

"""
以折线的上升或下降来表示统计数量的增减变化的统计图
特点：能够显示数据的变化趋势，反映事物的变化情况。
"""


def plot_v1():
    # 折线图（x，y）
    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [6, 9, 14, 21, 30, 41, 54, 69]
    z = [55, 105, 155, 205, 305, 355, 405]

    plt.plot(x, y)
    plt.plot(x, z)
    plt.xlabel('week')
    plt.ylabel('stock')
    plt.title('Stock Price')
    # plt.legend(['y = x**2 +5', 'z = x * 50 +5'])
    plt.show()


def plot_v2():  # 2.绘制折线图
    x = range(1, 10)
    y = [1, 3, 9, 12, 15, 23, 34, 31, 23]
    plt.plot(x, y)  # 传入x轴和y轴数据，通过plot绘制折线图
    plt.show()


def plot_v3():  # 3.设置折线的颜色和形状
    x = range(1, 10)
    y = [1, 3, 9, 12, 15, 23, 34, 31, 23]

    #
    # color: 折线颜色；可以设置16进制颜色码或者英文单词
    # alpha: 折线透明度； 范围 0~1
    # linestyle: 折线样式
    #            -  实线（solid）
    #            -- 短线（dashed）
    #            -. 短点相间线（dashdot）
    #            :  虚点线(dotted)
    # linewidth： 折线宽度
    plt.plot(
        x, y, color='pink', alpha=0.6, linestyle='--', linewidth=2
    )  # 传入x轴和y轴数据，通过plot绘制折线图

    plt.show()


def plot_v4():  # 4.设置折点
    x = range(1, 10)
    y = [1, 3, 9, 12, 15, 23, 34, 31, 23]

    plt.plot(
        x, y, marker='o', color='pink',
        markersize=15, markeredgecolor='g', markeredgewidth=3
    )  # 传入x轴和y轴数据，通过plot绘制折线图
    """
    折点样式(marker)选择
    character	description
    '-'	实线样式
    '--'	短线样式
    '-.'	点短线样式
    ':'	虚线样式
    '.'	点标记
    ','	像素标记
    'o'	圆形标记
    'v'	三角向下标记
    '^'	三角向上标记
    '<'	三角向左标记
    '>'	三角向右标记
    's'	方形标记
    'p'	五边形标记
    '*'	星号标记
    'h'	六边形标记
    'H'	加粗六边形标记
    '+'	加号标记
    'x'	x标记
    'D'	加粗菱形标记
    'd'	菱形标记
    '|'	|标记
    '_'	下划线标记
    """
    plt.show()


def plot_v5():  # 5.设置图片大小
    from matplotlib import pyplot as plt
    x = range(1, 10)
    y = [1, 3, 9, 12, 15, 23, 34, 31, 23]

    #
    # 设置图片(画布)大小
    #   figsize: 指定画布的宽和高，单位：英寸
    #   dpi：指定绘图对象的分辨率，即每英寸多少个像素点，缺省值为80    1英寸等于2.5cm
    #
    plt.figure(figsize=(20, 8), dpi=80)
    plt.plot(
        x, y, marker='_', color='pink',
        markersize=12, markeredgecolor='g', markeredgewidth=3
    )  # 传入x轴和y轴数据，通过plot绘制折线图

    # # plt.show()会释放figure资源，如果在显示图像之后报出图像将会得到一张空的图片
    # plt.show()

    plt.savefig('./t1.png')
    # 可以保存为矢量图格式，矢量图在网页中放大不会有锯齿
    # plt.savefig('./t1.svg')


def plot_v6():  # 6.设置折线的x轴和y轴刻度
    x = range(1, 13)
    y = [1, 3, 9, 12, 15, 23, 34, 31, 23, 28, 27, 30]

    plt.xticks(x)  # 设置x轴刻度
    plt.yticks(y)  # 设置y轴刻度

    #
    # 处理mac系统中文乱码问题： 在fname参数中指定字体路径 生成字体对象
    #
    my_font = font_manager.FontProperties(fname='msyh.ttc', size=16)
    xtick_labels = ['{}月'.format(i) for i in x]
    ytick_labels = ['{}万'.format(i) for i in y]
    plt.xticks(x, xtick_labels, fontproperties=my_font, rotation=45)
    plt.yticks(y, ytick_labels, fontproperties=my_font)

    # 这两句是处理Windows系统中文乱码问题, 直接调用系统中字体
    # plt.rcParams['font.sans-serif'] = ['SimHei']
    # plt.rcParams['axes.unicode_minus'] = False

    # 设置x轴标签，并让字体旋转45度
    # xtick_labels = ['{}月'.format(i) for i in x]
    # ytick_labels = ['{}万'.format(i) for i in y]
    # plt.xticks(x, xtick_labels, rotation=45)
    # plt.yticks(y, ytick_labels)

    plt.plot(
        x, y, marker='o', color='pink',
        markersize=10, markeredgecolor='g', markeredgewidth=2
    )  # 传入x轴和y轴数据，通过plot绘制折线图
    plt.show()

    # plt.savefig('./t2.png')
    # 可以保存为矢量图格式，矢量图在网页中放大不会有锯齿
    # plt.savefig('./t2.svg')


def plot_v7():  # 7.一图多线
    x = range(1, 13)
    y1 = [1, 3, 9, 12, 15, 23, 34, 31, 23, 28, 27, 30]
    y2 = [3, 2, 12, 21, 23, 4, 32, 30, 28, 18, 21, 31]
    my_font = font_manager.FontProperties(fname='msyh.ttc', size=16)

    plt.plot(x, y1, color='red', label='小明')
    plt.plot(x, y2, color='blue', label='小方')

    # plt.rcParams['font.sans-serif'] = ['SimHei']
    # plt.rcParams['axes.unicode_minus'] = False

    plt.xticks(x, ['{}月'.format(i) for i in x])

    plt.ylabel('销售额(万)')  # y轴标题
    plt.title('每月销售额')  # 图片标题

    # 绘制网格
    # alpha设置透明度，也可以设置网格线的样式
    plt.grid(alpha=0.4)

    # 添加图例
    # 设置位置loc: upper left、lower left、center left、upper center
    plt.legend(loc='upper left')

    plt.show()


def plot_v8():  # 8.一图多个坐标系子图

    x = np.arange(1, 100)
    fig = plt.figure(figsize=(20, 10), dpi=80)  # 新建一个20*10，像素为80的画布

    ax1 = fig.add_subplot(2, 2, 1)  # 新建第一个子图  将画布分为两行两列，占据第一个位置
    ax1.plot(x, x)

    ax2 = fig.add_subplot(2, 2, 2)  # 第二个子图
    ax2.plot(x, x ** 2)
    # 添加网格，并设置虚线样式宽度为1，透明度0.4
    ax2.grid(color='red', linestyle='--', linewidth=1, alpha=0.4)

    ax3 = fig.add_subplot(2, 2, 3)  # 第三个子图
    ax3.plot(x, np.log(x))

    plt.show()


def plot_v9():  # 9.设置坐标轴范围
    x = np.arange(-10, 11)
    plt.plot(x, x ** 2)
    # plt.xlim([-3, 8])  # 调整x轴左右范围
    # plt.xlim(xmin=-3)
    # plt.xlim(xmax=5)
    plt.xlim(xmin=0, xmax=8)  # 设置x轴最小范围和最大范围
    plt.ylim(ymin=0)  # 设置y轴最小范围
    plt.show()


def plot_v10():  # 10.改变坐标轴默认显示方式
    x = range(-5, 5)
    y = range(0, 20, 2)

    ax = plt.gca()  # 获取当前图像

    # 设置图像的边界线
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_color('blue')
    ax.spines['left'].set_color('red')

    # 设置底边的移动范围，移动到y轴的0位置，'data':移动轴的位置到交叉轴的指定坐标
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))

    plt.plot(x, y)
    plt.show()

# plot_v2()
# plot_v3()
# plot_v4()
# plot_v5()
# plot_v6()
# plot_v7()
# plot_v8()
# plot_v9()


plot_v10()
