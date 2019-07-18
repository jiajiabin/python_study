# 编写函数※※传入三个单词，用空格隔开，将三个单词，用[]进行包裹
# 传入 hello world good
# 返回 [hello][world][good]
def bag_word(str1):
    list1 = str1.split(" ")
    str2 = ""
    while 1:
        if '' in list1:
            list1.remove('')
        else:
            break
    for i in list1:
        j = "[" + i + "]"
        str2 += j
    return str2


print(bag_word("hellw world good"))
