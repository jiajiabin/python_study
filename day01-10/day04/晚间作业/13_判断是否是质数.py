# 输入一个正整数，判断这个数是否是质数
a = int(input())
j = 0
if 0 < a <= 2:
    print("是质数")
elif a > 2:
    for i in range(2, a):
        if a % i == 0:
            j += 1
    if j:
        print("不是质数")
    else:
        print("是质数")
else:
    print("不是正整数")
