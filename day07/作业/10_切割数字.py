# .编写函数传入10个数字，10个数字都用空格隔开，将10个数字从大到小返回
def cut_num(str1):
    if " " not in str1:
        return str1
    else:
        list1 = str1.split(" ")
        list2 = []
        while 1:
            if '' in list1:
                list1.remove('')
            else:
                break
        for i in range(len(list1)):
            max1 = max(list1)
            list1.remove(max1)
            list2.append(max1)
        return list2


print(cut_num("1 3   4 5"))
