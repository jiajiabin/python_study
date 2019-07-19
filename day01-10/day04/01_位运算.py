print(8 & -8)
print(8 | -8)
print(~8)
print(8 ^ -8)
print(8 << 2)
print(-8 << 2)

print((1 << 2) & 5 != 0) # 查看5的第2位 101
# 101 -> 111
a = 5
a |= 1 << 1
print(a)

