#输入一个正整数，判断这个数是不是偶数
a = int(input("输入"))
if a <= 0:
    print("不是正整数")
elif a % 2 == 0:
    print("是偶数")
else:
    print("不是偶数")