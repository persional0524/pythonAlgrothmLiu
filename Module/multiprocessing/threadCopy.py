#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   threadCopy.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/14 11:23 下午   Lita       1.0         None
"""

# 多线程，实现高并发的效果
import os
import threading as td


def copy_file(file_name, source_dir, dest_dir):
    # 1.拼接文件路径和目标文件路径
    source_path = source_dir + '/' + file_name
    dest_path = dest_dir + '/' + file_name
    # 2.打开源文件和目标文件
    with open(source_path, "rb") as source_file:
        with open(dest_path, "wb") as dest_file:
            # 3.循环读取文件到目标路径
            while True:
                date = source_file.read(1024)  # 1K
                if date:
                    dest_file.write(date)
                else:
                    break


if __name__ == '__main__':
    source_dir = "/Users/liutao/PycharmProjects/pythonAlgrothmLiu/Algrothm/sort"
    dest_dir = "/Users/liutao/Desktop/test"
    try:
        os.mkdir(dest_dir)
    except:
        print("目标目录已经存在了.")
    file_list = os.listdir(source_dir)

    for file_name in file_list:
        # copy_file(file_name, source_dir, dest_dir)
        # 创建子线程，震开销更小，功能一样可以实现
        sub_thread = td.Thread(target=copy_file, args=(file_name, source_dir, dest_dir))
        sub_thread.start()
