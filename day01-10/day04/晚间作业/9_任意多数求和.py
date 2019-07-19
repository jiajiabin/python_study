#输入任意多的数，用0结尾，求这些数的和
sum = 0
while 1:
    a = int(input("输入"))
    sum += a
    print("和为",sum)
    if a == 0:
        break