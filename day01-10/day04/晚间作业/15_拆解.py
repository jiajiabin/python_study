'''
输入1个大于1的正整数，求如果将这个数拆成两个正整数的和，如何拆使两数的乘积最大
比如5 可以拆成 1 + 4 或 2 + 3
输出乘积
'''
a = int(input())
if a >= 1:
    for i in range(1,int(a / 2) + 1):
        max = 1 * (a - 1)
        if max < i * (a - i):
            max = i * (a - i)
    print(max)
else:
    print("输入值不正确")


