# 编写函数※传入一个语句，由单词和空格组成，将每个单词逆序再拼回一个字符串
# 传入：hello world
# 返回：olleh dlrow
def reversed_order(str1):
    list1 = str1.split(" ")
    str2 = ""
    for i in list1:
        i = i[::-1] + " "
        str2 += i
    return str2


print(reversed_order("hello world"))
