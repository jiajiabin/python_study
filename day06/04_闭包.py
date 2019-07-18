# 将一个函数声明在另一个函数当中，这个内部的函数称为闭包函数

def print_hello():
    print("hello!")
    def print_world():
        print("world!")
    # 在函数外面声明的变量，不能使用在函数里面，只能通过传参，把值传进来
    # 同样声明在函数内部的变量，也不能使用在函数的外面，我们称函数拥有自己的【作用域】。
    # if for while等流程控制语句没有自己的[作用域]
    # 闭包函数只能在声明所在的函数中调用
    print_world()

print_hello()



