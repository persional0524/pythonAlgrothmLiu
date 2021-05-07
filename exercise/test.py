#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   test.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/28 12:30 下午   Lita       1.0         None
"""

"""

运行a[1::3]，从index=1开始，步
幅为3，到一个新的数组b，b=[2,5]；
"""
a = [1, 2, 3, 4, 5]

sums = sum(map(lambda x: x + 3, a[1::3]))
print(lambda x: x + 3, a[1::3])
print(sums)

for i in range(5):
    i += 1
    print("-------")
    if i == 3:
        continue
    print(i)


def func(s, i, j):
    if i < j:
        func(s, i + 1, j - 1)
        s[i], s[j] = s[j], s[i]


def main():
    a = [10, 6, 23, -90, 0, 3]
    func(a, 0, len(a) - 1)
    for i in range(6):
        print(a[i])
        print("\n")


main()


def test(a, b, *args):
    print(a)
    print(b)
    print(args)


test(11, 22, 33, 44, 55, 66, 77, 88, 99)

info = {'name': '班长', 'id': 100, 'sex': 'f', 'address': '北京'}
age = info.get('age')
print(age)
age = info.get('age', 18)
print(age)




