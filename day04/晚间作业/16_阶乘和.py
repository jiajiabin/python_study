#输入两个数，求两个数的阶乘和
a = int(input())
b = int(input())
m = 1
n = 1
for i in range(1,a+1):
    m *= i
for i in range(1, a + 1):
    n *= i
print(m + n)