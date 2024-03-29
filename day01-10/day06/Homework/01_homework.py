# •    写一个函数，接受一个整数，输出这个整数是几位数
# 获得这个数
# 1 - --->
# 1 // 10 = 0 - ---> 一位数
# 0 // 10 = 0 - ---> 1
# 9 // 10 = 0 - ---> 1
#
# 10 // 10 == 1
# 1 // 10 == 0 - ---> 2
#
# 100 // 10 == 10
# 10 // 10 = 1
# 1 // 10 = 0 - --->

def function01(x):
    n = 0
    while True:
        if 0 < x // 10 ** n < 10:
            break
        else:
            n += 1

    print(x, "是", n + 1, "位数!")


#
#
# •    一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同

def fucntion02(n):
    if n < 10000 or n >= 100000:
        return False
    bit0 = n % 10
    bit1 = n // 10 % 10
    bit3 = n // 1000 % 10
    bit4 = n // 10000
    return bit0 == bit4 and bit1 == bit3

print(fucntion02(12321))
#
# •    封装一个功能，判定一个数是不是质数【只能被1和本身整除】

def  isPrime(n):
    if n <= 1 or not isinstance(n, int):
        return False
    if n == 2:
        return True
    for i in range(2, n):       # 如果循环提前退出，表示2-(n-1)有至少一个数能整除n
        if n % i == 0:
            return False
    return True                 # 循环正常退出，说明除了1，和n本身，没有数能整除n

print(isPrime(17))
#
# •    有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，
# 他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
# F(1) = 10
# F(2) = F(1) + 2
# F(3) = F(2) + 2
#
# F(n) = F(n - 1) + 2

def function():
    x = 10
    for i in range(2, 6):   # i是第几个人，x是岁数
        x += 2
    return x




# 5.
# 定义函数实现如下要求
# 例如：输入2，5，则求2 + 22 + 222 + 2222 + 22222
# 的和
# 规律:
# 1
# 位数
# 2
# 2
# 位数
# 22 + 2
#
# 2
# 22
# 222
# 使用递归写规律:
# 1 - - 2
# 2 - - 2 * 10 ^ 2 - 1 + 2
# F(1) = 2
# F(2) = 2 * 10 ** (2 - 1) + F(1)
# F(3) = 2 * 10 ** (3 - 2) + F(2)
#
# 2
# 22 + 2
# Sum(1) = 2
# Sum(2) = 22 + sum(1)
# Sum(3) = 222 + sum(2)
