import random
'''
练习:
1.将12345的第5位设为1
2.将12345的第7位设为0
3.查看12345的第6为是0还是1
'''
a0 = 12345
a1 = 1 << 5 | a0
print(a1)
a2 = ~(1 << 7) & a0
print(a2)
if a0 & (1 << 6):
    print("第六位是1")
else:
    print("第六位是0")
'''
4.生成一个随机数(-100，100)，打印这个随机数，并打印这个随机数的第3位
5.生成两个随机数(-100, 100)，打印着两个随机数，并说明两个数中较大的
'''
b1 = random.randint(-100,100)
print(b1)
if b1 & (1 << 3):
    print("第3位是1")
else:
    print("第3位是0")

c1 = random.randint(-100,100)
c2 = random.randint(-100,100)
print("c1 =",c1,"c2 =",c2)
if c1 > c2:
    print("c1大")
elif c1 == c2:
    print("一样大")
else:
    print("c2大")