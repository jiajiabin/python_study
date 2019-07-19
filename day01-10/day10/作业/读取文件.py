# 读取文件

# 打开文件
file = open("dict.txt", "r", encoding="UTF-8")

# 将所有数据一次性读入内存，生成一个列表。源文件中一行文字，是列表的一个元素
for i in range(14000):
    x = file.readlines(1)
    print(x)


# ['\ufeffAfrica\tn. 非洲\n']
# ['Aids\tn. 爱滋病\n']
# ['America\tn. 美洲\n']
# ['April\tn. 四月\n']
# ['Arab\tadj. 阿拉伯的\\nn. 阿拉伯人\n']
# ['Asia\tn. 亚洲\n']
"""
l1 ='Arab\tadj. 阿拉伯的\\nn. 阿拉伯人\n'.split("\t")
print(l1)
s1 = l1[1]
print(s1)
print("\\n"in s1)
l2 = s1.split("\\n")
print(l2)
"""