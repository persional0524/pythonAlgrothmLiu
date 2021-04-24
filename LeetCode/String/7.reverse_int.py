#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    :   7.reverse_int.py    
@Contact :   liutao0705@live.com
@License :   (C)Copyright 2021-2022

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/7 3:00 下午   Lita       1.0         None
"""
"""
python 的位运算符：

(a & b)
按位与运算符：参与运算的两个值，如果两个相应位都为 1，则该位的结果为 1，否则为 0 。
输出结果 12 ，二进制解释： 0000 1100
(a | b)
按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。 
输出结果 61 ，二进制解释： 0011 1101
(a ^ b)
按位异或运算符：当两对应的二进位相异时，结果为 1 
输出结果 49 ，二进制解释： 0011 0001
(~a )
按位取反运算符：对数据的每个二进制位取反，即把 1 变为 0，把 0 变为 1 。~x 类似于 -x-1 
输出结果 -61 ，二进制解释： 1100 0011，在一个有符号二进制数的补码形式。
a << 2 
左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补 0。
输出结果 240 ，二进制解释： 1111 0000
a >> 2
右移动运算符：把 ">>" 左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数 
输出结果 15 ，二进制解释： 0000 1111
python 赋值运算符：

*= 乘法赋值运算符 c *= a 等效于 c = c * a
/= 除法赋值运算符 c /= a 等效于 c = c / a
%= 取模赋值运算符 c %= a 等效于 c = c % a
**= 幂赋值运算符 c **= a 等效于 c = c ** a
//= 取整除赋值运算符 c //= a 等效于 c = c // a

"""


def reverse_int_v1(num):
    res = 0
    while num > 0:
        res = res * 10
        print(res)
        res += num % 10
        print(" " + str(res))
        num = num // 10
        print("  " + str(num))

    return res


"""
 1 str = '0123456789'  #str[start:stop:step]   遵循【左闭右开】规则
 2 
 3 print(str[0:3])     #截取第一位到第三位的字符                 　　　　　　　　　　#012
 4 print(str[1:5])     #截取第二位到第六位之前的字符              　　　　　　　　　　#1234
 5 print(str[:])       #截取字符串的全部字符                     　　　　　　　　   #0123456789
 6 print(str[6:])      #截取第七个字符到结尾                     　　　　　　　   　#6789
 7 print(str[:-3])     #截取从头开始到倒数第三个字符之前           　　　　　　　   　#0123456
 8 print(str[2])       #截取第三个字符                           　　　　　　      #2
 9 print(str[-1])      #截取倒数第一个字符                    　　　　　　　　      #9
10 print(str[::-1])    #创造一个与原字符串顺序相反的字符串        　　　　　　　  　  #9876543210
11 print(str[-3:-1])   #截取倒数第三位与倒数第一位之前的字符       　　　　　　　 　  #78
12 print(str[-3:])     #截取倒数第三位到结尾                    　　　　　　　   　 #789
13 print(str[:-5:-3])  #逆序截取，步长为3                     　　　　　　　　　　  #96
14 print(str[9:0:-1])  #逆序截取，起始值为列表的第10为数，到列表第1位数之前的数结束，　　#987654321
15 print(str[0:12])    #截取全部元素
"""


def reverse_int_v2(x):
    if -10 < x < 10:
        return x
    str_x = str(x)
    print(str_x)
    # if 正数
    if str_x[0] != '-':
        # 切片，字符串倒序输出
        str_x = str_x[::-1]
        print(str_x)
        x = int(str_x)
    # 负数
    else:
        # 字符串倒序输出
        str_x = str_x[:0:-1]
        print(str_x)
        x = int(str_x)
        x = -x
    return x if -2147483648 < x < 2147483647 else 0


def reverse_int_v3(x):
    y, res = abs(x), 0
    # 则其数值范围为 [−2^31,  2^31 − 1]
    boundry = (1 << 31) - 1 if x > 0 else 1 << 31
    while y != 0:
        res = res * 10 + y % 10
        if res > boundry:
            return 0
        y //= 10
    return res if x > 0 else -res


print(reverse_int_v2(-12300))
