# 编写函数传入一个字符串，判断字符串中有多少aba
# 传入 ababa
# 返回 2
def count_num(str1):
    num = 0
    m = 0
    while 1:
        if "aba" in str1[m:]:
            n = str1[m:].find("aba")
            num += 1
            m += n+2
        else:
            break
    return num
print(count_num("ababababbbaba"))
