#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   config_handler.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/25 2:17 下午   Lita       1.0         None
"""
import yaml

"""
02 yaml语法规则
基本语法规则：

大小写敏感；
使用缩进表示层级关系；
缩进时不允许使用Tab键，只允许使用空格；
缩进的空格数目不重要，只要相同层级的元素左侧对齐即可；
# 表示注释，从这个字符一直到行尾，都会被解析器忽略；

03 yaml数据结构
对象：键值对的集合，又称为映射（mapping）、哈希（hashes） 、字典（dictionary）；
数组：一组按次序排列的值，又称为序列（sequence） 、列表（list）；
纯量（scalars）：单个的、不可再分的值；

▌对象

Map（属性和值）（键值对）的形式：

key:(空格)value ：表示一对键值对，空格不可省略。

person:
    name: vivi
    age: 18
一行写法：
person:{name: vivi，age: 18}
相当于JSON格式：
{"name":"vivi","age":18}
▌数组

一组连词线开头的行，构成一个数组。数组前加有 “-” 符号，符号与值之间需用空格分隔。

color:
   - red
   - blue
   - green
一行写法：
color: [red,blue,green]
相当于JSON：

["red","blue","green"]
▌纯量

单个的、不可再分的值。（如：字符串、bool值、整数、浮点数、时间、日期、null等）

n1: 8
n2: 8.8
n3: true
n4: false
n5: 'vivi'

"""

class YamlHandler:
    def __init__(self, file):
        self.file = file

    def read_yaml(self, encoding='utf-8'):
        """读取yaml数据"""
        with open(self.file, encoding=encoding) as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)

    def write_yaml(self, data, encoding='utf-8'):
        """向yaml文件写入数据"""
        with open(self.file, encoding=encoding, mode='w') as f:
            return yaml.dump(data, stream=f, allow_unicode=True)


if __name__ == '__main__':
    data = {
        "user": {
            "username": "vivi",
            "password": '123456'
        }
    }

    # 读取config.yaml配置文件数据
    read_date = YamlHandler('../Config/config.yaml').read_yaml()
    write_date = YamlHandler('../Config/config1.yaml').write_yaml(data)
    print(read_date)
