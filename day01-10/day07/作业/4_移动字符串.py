# 编写函数传入一个字符串，和一个数字n，将字符串全部字符左移n位，最左侧的字符移到右侧
# 传入 abcdefg 3
# 返回 defgabc
def move_string(str1, num1):
    str2 = str1[:num1]
    str3 = str1[num1:]
    return str3 + str2


print(move_string("abcdef", 3))
