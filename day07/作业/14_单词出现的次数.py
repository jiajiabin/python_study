# 编写函数※传入一个单词和一个语句，找出单词在语句中出现的次数
def count_num(str1, str2):
    num = 0
    m = 0
    while 1:
        if str1 in str2[m:]:
            n = str2[m:].find(str1)
            num += 1
            m += n + 3
        else:
            break
    return num


print(count_num("abc", "abcabcdjfhiabcuwdababcaabc"))
