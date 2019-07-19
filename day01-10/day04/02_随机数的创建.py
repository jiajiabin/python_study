import random           # 官方模块，提供创建随机数的函数

# 创建一个随机的整数
n1 = random.randint(-5, 5)  # 最常用
print(n1)

# 从字符串中随机取出一个字符
n2 = random.choice("abcdefg")
print(n2)
s = "abcdefg"
n2 = random.choice(s)
print(n2)

# 从列表中，随机取一个元素
n3 = random.choice([1, 2, 3, 4, 5])
print(n3)
l = [1, 2, 3, 4, 5]
n3 = random.choice(l)
print(n3)

# 从列表中，随机取多个元素
n4 = random.sample([1, 2, 3, 4, 5], 2)
print(n4)
