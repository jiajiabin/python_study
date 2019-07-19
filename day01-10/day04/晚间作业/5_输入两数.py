'''
输入两个数
如 输入 3 4
则求 3 + 33 + 333 + 3333
'''
a = int(input())
b = int(input())
c = 0
a1 = a
for i in range(1,b+1):
    if i != 1:
        a1 += a * (10 ** (i - 1))
    c += a1
print(c)