import random

# 练习:
# 1.将12345的第5位设为1
a = 12345
a |= 1 << 5
print(a)

# 2.将12345的第7位设为0
a = 12345
a &= ~(1 << 7)
print(a)

# 3.查看12345的第6为是0还是1
a = 12345
ret = a & (1 << 6)
if ret:
    print(1)
else:
    print(0)

#
# 4.生成一个随机数(-100，100)，打印这个随机数，并打印这个随机数的第3位
n = random.randint(-100, 100)
# 找出随机数的第三位
m = int(n & (1 << 3) != 0)
print(n, m)


# 5.生成两个随机数(-100, 100)，打印着两个随机数，并说明两个数中较大的
a, b = random.randint(-100, 100), random.randint(-100, 100)
print(a, b)
if a > b:
    print(a, "比较大")
else:
    print(b, "比较大")



