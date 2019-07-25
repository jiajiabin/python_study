def add(a, b):
    return a + b


x = add
print(x(1, 2))
# 将函数赋值给一个变量，调用这个变量，就和调用这个函数是一样的


# 传参就是赋值，能赋值，就能传参
def good(a):        # a = add
    print(a(3, 4))


good(add)
