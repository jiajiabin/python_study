# 不是每一个创建的变量，在程序的任何位置都能使用的
# 变量的作用域决定了变量的可用范围(代码范围)
a = 9   # 全局作用域
def fucntion2():        # 全局作用域
    a = 11 # 闭包外函数作用域
    def function():     # 局部作用域
        # 函数里面叫做局部作用域Local
        a = 10
        # print(a)

    def do_it():
        nonlocal function       # 引用闭包外作用域的数据
        global a                # 引用全局作用域的数据
        print(a)
    do_it()

fucntion2()


print("123")        # 内置作用域

print(sum([1, 2, 3]))

# python当中只有函数会创建作用域，类、for if都不会产生作用域

