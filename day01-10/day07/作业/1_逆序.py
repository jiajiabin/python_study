# 编写函数传入一个字符串，将他逆序返回
# 传入 abc
# 打印 cba
def reversed_order(str):
    for i in range(len(str)):
        print(str[len(str) - 1 - i], end="")


reversed_order("asdcd")
