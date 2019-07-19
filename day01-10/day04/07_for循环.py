# python中的for循环格式特殊，用法非常简单

# 使用for循环打印5个hello world
# 【注】while能做的，for都能做，反过来也一样。
for i in range(5):
    print("hello world!", i)
# i是循环中自动加1的变量，i这个变量名是可以自定义的
# 【注】range(5)循环执行5次，i的值是0-4

# 规定变量i的范围 范围区间左闭右开
for i in range(3, 10):  # 范围 3-9
    print(i)

# 还可以自定义i每次循环增加的值，这个值被称为步数(stepper)
for i in range(1, 10, 2):
    print(i)

# 如果range的范围start>end，默认循环不执行，但是，如果stepper是负数，循环仍可执行
for i in range(5, 1, -1):
    print("good!", i)


# break和continue也可应用于for循环，其含义不变
# 打印100以下所有正整数，跳过7的倍数
for i in range(1, 101):
    if i % 7 == 0:
        continue
    print(i)












