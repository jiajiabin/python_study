#求1/1 + 1/2 + 1/3 + 1/10 的值
a = 10
b = 0
for i in range(1,a+1):
    b += 1 / i
print(b)