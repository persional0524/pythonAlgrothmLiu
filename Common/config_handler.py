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
