# 2.封装函数 并且写出其对应的匿名函数简化
# 	a. 将小写字母转化为大写字母  [不用考虑传入其他符号]


def change_letter(str):
    letter_str = str
    change_str = ""
    list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    list2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
    for i in letter_str:
        if i in list1:
            a = list1.index(i)
            change_str += list2[a]
        else:
            change_str += i
    return change_str


# print(change_letter(str(input("输入"))))

x = str(input("输入"))
y = lambda x: x.upper()
print(y(x))
