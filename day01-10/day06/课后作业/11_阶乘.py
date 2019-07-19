sum = 1
for i in range(1, 51):
    num = 1
    for j in range(1, i + 1):
        num *= i
    sum += 1 / num
print(sum)

sum = 1
n = 0
while 1:
    n += 1
    m = 1
    sum1 = 1
    while (m < n) or (sum1 < 10 ** 4):
        sum1 *= m
        m += 1
        sum += 1 / sum1
    if sum1 > 10 ** 4:
        break
print(sum)
