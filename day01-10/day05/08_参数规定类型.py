def add(a, b):
    return a + b

print(add(1, 2))
print(add("abc", "bcd"))


# python允许编写函数时，规定参数的类型
def prime(a: int, b: int):
    return a ** b

# print(prime("abc", "bcd"))


# 如果函数的每个参数类型都不同，有的时候，也用这种方式规定类型
def function(str, int):
    return str * int


print(function("abc", 5))

