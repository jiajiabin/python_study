# 封装一个功能，判定一个数是不是质数【只能被1和本身整除】
def prime(a):
    j = 0
    if 1 < a <= 2:
        print("是质数")
    if a == 1:
        print("1既不是质数也不是合数")
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


while 1:
    print(prime(int(input("输入："))))
