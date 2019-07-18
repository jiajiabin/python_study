'''
输入一个正整数，分解质因数
如输入 90
输出 90=2X3X3X5
'''
a = int(input())
a1 = a
b = []
if a >= 2:
    while a > 1:
        for i in range(2,a+1):
            if a % i == 0:
                b.append(i)
                a /= i
                a = int(a)
                break
    if len(b) == 1:
        print("%d是质数",a1)
    else:
        c = b[-1]
        b.pop()
        print(a1, '= ',end='')
        for j in b:
            print(j,'*',end='')
        print(c)
elif a == 1:
    print("1是质数")
else:
    print("不是正整数")