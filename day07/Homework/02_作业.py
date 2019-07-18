# 1.编写一个函数参数传入一个秒数，返回时间字符串
# 传入：61
# 返回：00:01:01
def seconds_to_time(seconds):
    h = seconds // 3600
    m = seconds % 3600 // 60
    s = seconds % 60

    return "%.2d:%.2d:%.2d" % (h, m, s)

print(seconds_to_time(786))


# 2.编写不定长参数函数，传入n个正整数，返回最大公约数
def max_reduce(*n):
    r = n[0]
    while True:
        all = True   # 假设n中所有的数都能被r整除
        for i in n:
            if i % r != 0:
                all = False
                break
        if all:
            return r
        else:
            r -= 1

print(max_reduce(8, 12, 16))




# 3.编写函数，传入一个字符串，打印如下图形：
# 传入：ABCDE
# 打印:
#     A
#    BAB
#   CBABC
#  DCBABCD
# EDCBABCDE
def print_graphics(s):
    length = len(s)       # 这个函数可以知道字符串的长度，即字符串中有多少个字符
    for i in range(1, length + 1):
        print(" " * (length - i), end="")
        print(s[i - 1: 0: -1], end="")
        print(s[0:i])

print_graphics("ABCDE")












# 4.编写函数，传入三个数，返回三数的立方和
def get_sum(a, b, c):
    return a ** 3 + b ** 3 + c ** 3




def num_people():
    for m in range(1, 29):      # 男人的范围1 - 28人
        for w in range(1, 29):
            for c in range(1, 29):
                if m * 3 + w * 2 + c * 1 == 50 and m + w + c == 30:
                    men, women, children = m, w, c
                    print("男人:{} 女人:{} 小孩:{}".format(men, women, children))



num_people()
