# 编写函数传入一个字符串，将字符串中的所有数字都去掉
# 传入 abc123d4h4
# 返回 abcdh
def del_num(str1):
    str2 = ""
    for i in str1:
        if i not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            str2 += i
    return str2


print(del_num("awd12"))
