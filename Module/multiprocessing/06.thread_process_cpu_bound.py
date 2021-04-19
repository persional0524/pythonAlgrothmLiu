#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   06.thread_process_cpu_bound.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/19 6:24 下午   Lita       1.0         None
"""
import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

"""
质数又称素数。
一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数；否则称为合数（规定1既不是质数也不是合数）。
"""
PRIMES = [112272535095293] * 100


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def single_thread():
    for number in PRIMES:
        is_prime(number)


def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


def multi_process():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


if __name__ == '__main__':
    start = time.time()
    single_thread()
    end = time.time()
    print("single_thread,cost=", end - start, "seconds")

    start = time.time()
    multi_thread()
    end = time.time()
    print("multi_thread,cost=", end - start, "seconds")

    start = time.time()
    multi_process()
    end = time.time()
    print("multi_process,cost=", end - start, "seconds")
