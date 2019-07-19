'''
任意输入两个数，从较小的数，加到较大的数，求和
如输入：4 6
输出 15			（4 + 5 + 6）
'''
a = int(input())
b = int(input())
sum = 0
for i in range(a,b+1):
    sum += i
print(sum)