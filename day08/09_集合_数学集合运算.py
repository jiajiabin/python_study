# 集合可以整体进行数学运算

# 求交集
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s = s1.intersection(s2)         # 生成新的集合，s1、s2均不变
print(s)
print(s1)
print(s2)

s1.intersection_update(s2)      # s1变成交集，s2不变
print(s1)
print(s2)


# 求并集
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s = s1.union(s2)
print(s)
print(s1, s2)

s1.update(s2)
print(s1)
print(s2)


# 求非交集
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s = s1.symmetric_difference(s2)
print(s)
print(s1, s2)

s1.symmetric_difference_update(s2)
print(s1)
print(s2)


# 求差集       在第一个里面有，在第二个里面没有的
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s = s1.difference(s2)
print(s)
print(s1, s2)

s1.difference_update(s2)
print(s1)
print(s2)