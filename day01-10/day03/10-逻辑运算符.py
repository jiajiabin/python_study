# # and
# # 输入两个数m,n，若两个数均为正数，则，求m的n次幂
# m = input()
# n = input()
#
# # 强制类型转换并赋值
# _m = int(m)
# _n = int(n)
#
# if _m > 0 and _n > 0:
#     print("结果为", _m ** _n)
# else:
#     print("输入的数字不都是正数")


# 输入两个数m,n，若两个数中有正数，则，求m的n次幂
# m = input()
# n = input()
#
# _m, _n = int(m), int(n)
#
# if _m > 0 or _n > 0:
#     print("结果为", _m ** _n)
# else:
#     print("输入的数字没有正数")


# 输入一个数n，若n不是负数，则，求n开根号
n = input()
_n = int(n)

if not(_n < 0):
    print("结果为", _n ** 0.5)
else:
    print("输入的是负数")



