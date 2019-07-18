#输入一个正整数，判断这个数是不是2的幂数
a = int(input())
while 1:
    if a == 2:
        print("是2的幂数")
        break
    elif a < 2:
        print("不是2的幂数")
        break
    else:
        pass
    a /= 2