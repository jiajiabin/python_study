# 打印100以下所有的正整数，跳过个位是7的数，如17 27 37 等
for i in range(1, 101):
    if i % 10 == 7:
        continue
    print(i)

# 求 1 + 2 + 3... + 100的和
s = 0
for i in range(1, 101):
    s += i
print(s)
