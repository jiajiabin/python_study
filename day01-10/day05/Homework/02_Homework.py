# *1.1！+2！+3！+4!+5!+6! = ?
# 迭代法
# n, x, y = 0, 1, 0
# for i in range(6):
#     y = y + 1
#     x = x * y
#     n = n + x
# print(n)


# 2.任意输入两个数，从较小的数，加到较大的数，求和
# 如输入：4 6
# 输出 15			（4 + 5 + 6）
# n, m = int(input()), int(input())
#
# if n < m:
#     _min = n
#     _max = m
# else:
#     _min = m
#     _max = n
#
# x = 0
# for i in range(_min, _max + 1):
#     x += i
# print(x)


# 3.输入起始值，结束值和步数（step）数数
# 如输入：1 9 2
# 输出 1 3 5 7 9
# n, m, s = int(input()), int(input()), int(input())
# if n <= m:
#     m += 1
# else:
#     m -= 1
# for i in range(n, m, s):
#     print(i)

# 4.输入任意多的数，用0结尾，求这些数的和
# s = 0
# while True:
#     x = int(input())
#     if x == 0:
#         break
#     s += x
# print(s)

# 5.输入一个正整数，判断这个数是不是偶数
# n = int(input())
# if n % 2 == 0:
#     print("偶数")
# else:
#     print("奇数")


# 6.输入一个正整数，判断这个数是不是奇数
# n = int(input())
# if n % 2 == 0:
#     print("偶数")
# else:
#     print("奇数")

# *7.输入一个正整数，判断这个数是不是2的幂数
# n = int(input())
# while n > 1:
#     n /= 2      # 只有2的幂数，不断除2会等于1
#
# if n == 1:
#     print("是")
# else:
#     print("不是")

#位运算  1000  100000  100000   100
# n & （n - 1） == 0-> 是        10000 & 01111 == 0   11000  &  10111 == 10000

# *8.输入一个正整数，判断这个数是否是质数
# 1 5 7 11 13   157
# n = int(input())
# i = 2
# while i < n:
#     if n % i == 0:  # i是2到n-1，如果i能整除n，n是合数
#         break
#     i += 1
#
# if i == n:
#     print("质数")
# else:
#     print("合数")


# *9.输入一个正整数，分解质因数
# 如输入 90
# 输出 90=2X3X3X5
# 90 / 2  --> 45  / 2-? 45/ 3 --> 15 / 3 -- 5 / 3  --> 5 / 4 --> 5 / 5
n = int(input())
i = 2
s = str(n) + "="
while n > 1:
    if n % i == 0:
        n /= i
        # 能整除，n缩小，i不变，下次还除i
        # i是一个质因数
        s += str(i)
        if n > 1:
            s += "X"
    else:
        # 不能整出，n不变，i增加1
        i += 1
print(s)



# 10.输入1个大于1的正整数，求如果将这个数拆成两个正整数的和，如何拆使两数的乘积最大
# 比如5 可以拆成 1 + 4 或 2 + 3
# 输出乘积
# n = int(input())
# m = 0
# for i in range(1, n // 2 + 1):
#     j = n - i
#     if i * j > m:
#         m = i * j
# print(m)

# 11.输入两个数，求两个数的阶乘和
# a, b = int(input()), int(input())
# s1 = 1
# for i in range(1, a + 1):
#     s1 *= i
# s2 = 1
# for i in range(1, b + 1):
#     s2 *= i
# print(s1 + s2)


# 12.输入十分秒，打印这个时间往后，1小时的所有秒数
# 如输入：23：12：13
# 输出：23：12：14
# 	23：12：15
# 	...
h, m, s = int(input()), int(input()), int(input())
for i in range(60 * 60):
    s += 1
    if s == 60:
        s = 0
        m += 1
        if m == 60:
            m = 0
            h += 1
            if h == 24:
                h =0
    print(h, ":", m, ":", s)
