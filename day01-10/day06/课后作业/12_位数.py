num = int(input("输入"))
wei_shu = 0
while 1:
    if num < 10:
        wei_shu += 1
        break
    num //= 10
    wei_shu += 1
print(wei_shu)
