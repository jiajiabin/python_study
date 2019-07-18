# 函数可以被赋值。
def add(a, b):
    return a + b


x = add     # 将一个函数赋值给一个变量
print(type(x))

print(x(1, 2))  # 使用x和使用add，是一样的

# x被称为函数变量或者偏函数
