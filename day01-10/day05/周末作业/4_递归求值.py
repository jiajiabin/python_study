"""
定义函数实现如下要求
例如：输入2，5，则求2 + 22 + 222 + 2222 + 22222
的和规律:
1位数2
2位数22
2
22
222
"""


def recursion(a, b):
    c = 0
    a1 = a
    for i in range(1, b + 1):
        if i != 1:
            a1 += a * (10 ** (i - 1))
        c += a1
    return c


while 1:
    print(recursion(int(input("输入：")), int(input("输入："))))