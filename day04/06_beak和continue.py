# break
# 打印100以下的自然数，但是碰到24，提前退出
n = 0
while n <= 100:
    if n == 24:
        break
    print(n)
    n += 1
else:
    print("Over!")


print("---------------------------------------")
# continue
# 打印100以下所有的自然数，但是跳过24.
n = -1
while n < 100:
    n += 1
    if n == 24:
        continue
    print(n)

print("---------------------------------------")
# 3.打印100以下所有的正整数，跳过7的倍数
n = 0
while n < 100:
    n += 1
    if n % 7 == 0:  # 一个数除以7余0，该数是7的倍数
        continue
    print(n)
