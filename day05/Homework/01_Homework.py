# 1.打印100(包括)以下的所有自然数
# for i in range(101):
#     print(i)

# 2.打印100以下的正整数中7的倍数
# for i in range(1, 101):   # i是100以下所有的正整数
#     if i % 7 == 0:        # 如果i是7的倍数，就打印
#         print(i)

# 3.打印100以下所有的正整数，跳过7的倍数
# for i in range(1, 101):
#     if i % 7 == 0:
#         continue
#     print(i)

# 4.打印100以下所有的正整数，跳过带7的数，如17，71等
# for i in range(1, 101):
#     if i % 10 == 7 or i // 10 == 7:
#         continue
#     print(i)

# 5.打印100以下所有的正整数，跳过7的倍数和带7的数据
# for i in range(1, 101):
#     if i % 7 == 0 or i % 10 == 7 or i // 10 == 7:
#         continue
#     print(i)

# 6.输入一个数，打印三角形
# 如输入5
# 打印：
# *
# **
# ***
# ****
# *****
# n = int(input("请输入一个数:"))
# for i in range(n):
#     print("*" * (i + 1))


# 7.输入一个数，打印矩形
# 输入5
# 打印
# *****
# *****
# *****
# *****
# *****
# n = int(input())
# for i in range(n):
#     print("*" * n)


# 8.求1 + 2 + 3 + 4 + ... + 100的值
# n = 1
# for i in range(2, 101):
#     n += i
# print(n)

# 迭代法
# x, n = 0, 0
# for i in range(100):
#     x = x + 1
#     n = n + x
# print(n)



# 9.求10！
# n = 10
# for i in range(9, 1, -1):
#     n *= i
# print(n)

# 10.求1/1 + 1/2 + 1/3 + 1/10 的值
# n = 0
# for i in range(1, 11):
#     n += 1 / i
# print(n)

# *11.输入两个数
# 如 输入 3 4
# 则求 3 + 33 + 333 + 3333
# 迭代法
a = int(input())
b = int(input())
x, n = 0, 0
for i in range(b):
    x = x * 10 + a
    n = n + x
print(n)

# 12.打印出所有对称的五位数
# for i in range(10000, 100000):
#     bit0 = i % 10
#     bit1 = i // 10 % 10
#     bit3 = i // 1000 % 10
#     bit4 = i // 10000
#     if bit0 == bit4 and bit1 == bit3:
#         print(i)

