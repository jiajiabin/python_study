# 求交集
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 & s2)

# 求并集
print(s1 | s2)

# 求非交集
print(s1 ^ s2)

# 求差集
print(s1 - s2)

# 判断一个集合是否是另一个集合的子集
print({1, 2, 3}.issubset({1, 2, 3, 4}))
# 判断一个集合是否是另一个集合的超集
print({1, 2, 3, 4}.issuperset({1, 2, 3}))
