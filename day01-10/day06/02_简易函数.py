# 通过lambda关键字，创建简易函数

x = lambda a, b: a + b
# 冒号前面的是参数，冒号后面的是返回值
print(x(3, 4))

y = lambda a, b: (a ** 2 + b ** 2) ** 0.5
print(y(3, 4))