# 编写函数在上一题基础上，将每个单词首字母大写
# 传入 hello world
# 返回 Hello World.编写函数
def capital_letter(str1):
    n = 0
    while str1[n] == " ":
        n += 1
    if 96 < ord(str1[n]) < 123:
        str1 = str1.replace(str1[n], chr(ord(str1[n]) - 32))
    return str1


print(capital_letter(" asdw"))


def fun1(str2):
    return str2.capitalize()


print(fun1(' acwva '))
