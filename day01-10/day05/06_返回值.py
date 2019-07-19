# 返回值是为了将函数运算的结果返还回来，留待进一步计算

# def avg(a, b, c):
#     d = (a + b + c) / 3
#     return d        # 返回值是return后面跟随的表达式的值
#
# # 调用
# x = avg(5, 6, 7)    # 返回值就是函数调用表达式avg(5, 6, 7)的值
# print(x)

def avg(a, b, c):
    return (a + b + c) / 3

print(avg(5, 6, 7) + 1)


def print_num():
    for i in range(1, 101):
        if i == 24:
            return      # 提前结束函数
        print(i)

print_num()
print("Over!")


def return_num():
    for i in range(1, 101):
        if i == 24:
            return i      # 提前结束函数
        print(i)

ret = return_num()
print("Good", ret)


# 写一个求两数和的函数
def add(a, b):
    return a + b
