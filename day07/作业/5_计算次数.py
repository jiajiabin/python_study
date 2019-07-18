# 编写函数传入一个字符串，判断字符串中abc出现了多少次
def count_num(str1):
    num = 0
    m = 0
    while 1:
        if "abc" in str1[m:]:
            n = str1[m:].find("abc")
            num += 1
            m += n + 3
        else:
            break
    return num


print(count_num("abcabcdjfhiabcuwdababcaabc"))
