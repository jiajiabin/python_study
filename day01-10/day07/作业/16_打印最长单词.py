#编写函数※※传入多个单词，用空格分割，打印最长的一个单词，或多个单词
def print_word(str1):
    list0 = [" "]
    print(list0[0])
    list1 = str1.split(" ")
    while 1:
        if '' in list1:
            list1.remove('')
        else:
            break
    for i in list1:
        if len(list0[0]) < len(i):
            list0.clear()
            list0.append(i)
        elif len(list0[0]) == len(i):
            list0.append(i)
    return list0
print(print_word("adw awdav awda awfas awd"))