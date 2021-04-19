#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   03.lock_concurrent.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/19 3:48 下午   Lita       1.0         None
"""
import threading
import time

lock = threading.Lock()


class Account:
    # 构造函数
    def __init__(self, balance):
        self.balance = balance


"""
线程安全是指某个函数、函数库在多线程环境中被调用时。能够正确的处理多个线程之间的共享变量，使程序功能正确完成。
由于线程的执行随时会发生切换，就造成了不可预料的结果，出现线程不安全
"""


# 定义取钱函数
def draw(account, amount):
    with lock:
        if account.balance >= amount:
            # 一直会出错，sleep
            time.sleep(0.1)
            print(threading.current_thread().name, "取钱成功")
            account.balance -= amount
            print(threading.current_thread().name, "余额", account.balance)
        else:
            print(threading.current_thread().name, "取钱失败,余额不足")


if __name__ == '__main__':
    account = Account(1000)
    ta = threading.Thread(name="ta", target=draw, args=(account, 800))
    tb = threading.Thread(name="tb", target=draw, args=(account, 800))

    ta.start()
    tb.start()
