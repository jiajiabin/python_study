ls = ["零", "一", "二", "三", "四", "五"]

# 直接打印
print(ls)

# 求列表长度
print(len(ls))

# 遍历打印
for i in range(len(ls)):
    print(ls[i])

for i in ls:
    print(i)    # i就是列表元素

# 隔一个打印一个
for i in range(0, len(ls), 2):
    print(ls[i])

for i in ls[::2]:
    print(i)


