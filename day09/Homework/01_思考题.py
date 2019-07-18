# 兔子问题？
# 已知第一月有一对兔子，兔子长到第三个月，每月会生一对兔子，这对儿涨到第三个月也会开始生兔子
# 假设兔子都不死，问第n月共有多少兔子
#
# def question(n):
#     r1, r2, r3 = 2, 0, 0
#     for i in range(n):
#         r3 = r3 + r2
#         r2 = r1
#         r1 = r3
#     return r1 + r2 + r3
#
# print(question(5))
#
#
#
# #
# # 已知m个人，坐一列，循环报数，报道n，下一个人从1重新报。凡是报道n的退出
# # 问最后剩下的人是原来第几个人
# def question02(m, n):
#     ls = [0 for i in range(m)]  # 列表中是m个0， 列表中每个元素表示一个人
#     index = 0                   # 第0个人开始数数
#     count = 1
#     x = len(ls)                       # x表示剩余多少人
#     while x > 1:
#         if ls[index] != n:      # 只有这个人不是n，他才报数
#             ls[index] = count
#             if count == n:
#                 x -= 1          # 减少了一个人
#                 count = 1
#             else:
#                 count += 1
#         index += 1              # 每个人报完数，下一个人接着报，最后一个人报完了，第一个人接着报
#         if index == m:
#             index = 0
#
#     for i in range(len(ls)):
#         if ls[i] != n:
#             print("第%d个人" % (i + 1))
#
# question02(5, 3)



#
#
# 输入一个数打印图形
# 输入5
# 打印
#     *
#    * *
#   *   *
#    * *
#     *


def print_graphics(n):
    left = right = n // 2
    for i in range(n):
        for j in range(n):
            if j == left or j == right:
                print("*", end="")
            else:
                print("-", end="")
        print()
        if i > n // 2 - 1:
            left += 1
            right -= 1
        else:
            left -= 1
            right += 1

print_graphics(6)