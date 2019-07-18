# 作业：
# ※※※1.编写函数传入两个正整数，求两个数的最大公约数
def question01(a, b):
    _min = min(a, b)
    while True:
        if a % _min == 0 and b % _min == 0:
            return _min
        else:
            _min -= 1


# ※※※※2.编写函数传入一个正奇数，打印下列图形
# 传入5
# 打印
#   *
#  ***
# *****

def question02(n):
    for i in range(1, n + 1, 2):
        print(" " * ((n - i) // 2), end="")
        print("*" * i)

question02(7)


# ※3.编写函数传入一个字符串，将他逆序返回
# 传入 abc
# 打印 cba

def reverse(s: str):
    return s[::-1]

# ※※※※4.编写函数传入一个字符串，打印如下图形
# 传入 abcdefg
# 打印
# abcdefg
#      f
#     e
#    d
#   c
#  b
# abcdefg
def question04(s: str):
    print(s)
    n = len(s) - 2          # 空格个数
    for i in s[-2: 0: -1]:
        print(" " * n, end="")
        print(i)
        n -= 1              # 每行空格个数减少
    print(s)

question04("abcdefg")

# ※※5.编写函数传入一个字符串，将字符串中的所有数字都去掉
# 传入 abc123d4h4
# 返回 abcdh
def question05(s:str):
    n_s = ""
    for i in s:
        if i in "0123456789":
            pass    # if else elif for while 函数 当中如果没有语句，填一个pass
        else:
            n_s += i
    return n_s


# ※※6.编写函数传入一个字符串，和一个数字n，将字符串全部字符左移n位，最左侧的字符移到右侧
# 传入 abcdefg 3
# 返回 defgabc
def question06(s: str, n: int):
    n %= len(s)
    n_s = s[n:] + s[:n]
    return n_s



# ※※7.编写函数传入一个字符串，将重要信息放在[]之间，找出重要信息
# 传入 我是一个[好人]
# 返回 好人
# ※8.编写函数传入一个字符串，判断字符串中abc出现了多少次
# ※※※9.编写函数传入一个字符串，判断字符串中有多少aba
# 传入 ababa
# 返回 2

# ababa
def question09(s:str, cs:str):
    count = 0       # 计数器
    while True:
        ret = s.find(cs)
        if ret >= 0:
            count += 1
            s = s[ret + 1:]     # 提取s，下次循环，从刚才位置的后面开始找
        else:
            return count

# ※※※※※10.编写函数传入两个字符串，打印出最长的公有部分，如果出现并列最长，以第一个字符串首次出现为准
# 传入 abcdefg cdefghi
# 返回 cdefg
# 传入 abcdefg defgabc
# 返回 defg
# 传入 abcdefxyzhi  cdefqqxyzhxx
# 返回 cdef
def question10(s1: str, s2: str):
    longest = 0             # 最长公共部分的长度
    lstr = None
    for i in range(0, len(s1)):
        # 得到一个字符s1[i], 从s1[i] 开始，找到s1[i]-s1[i + n]在第二个字符串中出现的最长子串
        # abcdefg cdefghi
        count = 0
        for j in range(i + 1, len(s1) + 1):
            if s1[i: j] in s2:
                count += 1
                continue
            else:
                break
        if longest < count:
            longest = count
            lstr = s1[i: i + count]

    return lstr

print(question10("abcdefg", "cdefghi"))
print(question10("abcdefg", "defgabc"))
print(question10("abcdefxyzhi", "cdefqqxyzhxx"))







# ※11.编写函数传入一段英文文字，没有标点，单词间用单空格隔开，求，有多少个单词
def question11(s:str):
    # "hello world good"
    ls = s.split(" ")
    # ['hello', "world", "good"]
    return len(ls)

# ※※12.编写函数在上一题基础上，将每个单词首字母大写
# 传入 hello world
# 返回 Hello World.编写函数

def question12(s:str):
    # "hello world good"
    s = s.title()
    ls = s.split(" ")
    # ['Hello', "World", "Good"]
    return ls

#
# 作业：
# 1.编写函数※传入一段英文文字，没有标点，单词间用单空格或多空格隔开，求，有多少个单词
def question2_01(s: str):
    ls = s.split(" ")
    # "hello  world  good "
    #['hello', '', 'word', '', 'good', '']
    count = 0
    for i in ls:
        if i == "":
            pass
        else:
            count += 1
    return count

# 2.编写函数※※传入10个数字，10个数字都用空格隔开，将10个数字从大到小返回
def question2_02(i1, i2, i3, i4, i5, i6, i7, i8, i9, i10):
    ls = [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10]
    ls.sort(reverse=True)
    return ls


# 3.编写函数※※传入三个单词，用空格隔开，将三个单词，用[]进行包裹
# 传入 hello world good
# 返回 [hello][world][good]
def question2_03(s: str):
    ls = s.split(" ")
    while "" in ls:
        ls.remove("")
    return "[" + "][".join(ls) + "]"


# 4.编写函数※※※传入一个带中括号的时间，将时间转成秒数
# 传入[00:01:03]你是我的心
# 返回63->你是我的心
def question2_04(s: str):
    index01 = s.find("[")
    index02 = s.find("]")
    time_str = s[index01 + 1: index02]
    # 00:01:03
    l = time_str.split(":")
    seconds = int(l[0]) * 3600 + int(l[1]) * 60 + int(l[2])
    return "{}->{}".format(seconds, s[:index01] + s[index02 + 1:])

print(question2_04("[00:01:03]你是我的心"))

# 5.编写函数※※传入10个时间，找出最大的一个传入格式[00:00:00]

# 6.编写函数※传入一个单词和一个语句，找出单词在语句中出现的次数

# 7.编写函数※传入一个语句，由单词和空格组成，将每个单词逆序再拼回一个字符串
# 传入：hello world
# 返回：olleh dlrow
def question2_07(s: str):
    ls = s.split(" ")           #  ["hello", "world"]
    n_ls = []
    for i in ls:
        n_ls.append(i[::-1])    # ["olleh", "dlrow"]
    return " ".join(n_ls)

# 8.编写函数※※传入多个单词，用空格分割，打印最长的一个单词，或多个单词
def question2_08(s: str):
    ls = s.split(" ")
    longest = 0
    for i in ls:
        if len(i) > longest:
            longest = len(i)
    for i in ls:
        if len(i) == longest:
            print(i)
