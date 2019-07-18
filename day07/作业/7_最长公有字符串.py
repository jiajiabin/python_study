# 编写函数传入两个字符串，打印出最长的公有部分，如果出现并列最长，以第一个字符串首次出现为准
# 传入 abcdefg cdefghi
# 返回 cdefg
# 传入 abcdefg defgabc
# 返回 defg
# 传入 abcdefxyzhi  cdefqqxyzhxx
# 返回 cdef
def long_string(str1, str2):
    str3 = ""
    min_str = ""
    #判断str1，str2哪个短
    if len(str1) <= len(str2):
        min_str = str1
    else:
        min_str = str
    #找到最长公有片段
    for i in range(len(min_str)):
        for j in range(i,len(min_str)+1):
            if min_str[i:j] in str1 and min_str[i:j] in str2:
                if len(min_str[i:j]) > len(str3):
                    str3 = min_str[i:j]
    return str3

print(long_string("abcdefg", "cdefghi"))
print(long_string("abcdefg", "defgabc"))
print(long_string("abcdefxyzhi", "cdefqqxyzhxx"))