# 多继承时，如果不同的父类拥有相同的变量名或方法名，则会产生二义性
# 到底我们使用的时候，使用的是那个父类的属性和方法呢？

class Father:
    def __init__(self, a):
        self.__a = a
        self.__b = a ** 2
        self.x = 10

    def show(self):
        print("Father", self.__a, self.__b)

    def set_x(self, x):
        self.x = x


class Mother:
    def __init__(self, b, c):
        self.__c = c
        self.__b = b
        self.x = 11

    def show(self):
        print("Mother", self.__b, self.__c)

    def get_x(self):
        return self.x


class Child(Father, Mother):        # 谁写前面默认调用谁的方法
    def __init__(self, a, b, c):
        # 私有变量，即使继承了，在子类中也是两个变量，调用Father的函数，访问的是father的变量
        # 调用Mother类的函数，访问的是Mother的变量
        Mother.__init__(self, b, c)
        Father.__init__(self, a)
        # 对于子类可以访问的变量，保护变量和公有变量，多个父类同名变量，在子类中是一个变量。
        # 无论调用哪个父类方法修改这个变量都是修改同一个变量。

    def x_show(self):
        print(self.x)


c = Child(1, 2, 3)
c.show()
Mother.show(c)
# 如果参数是父类对象，传子类对象也可以。
c.x_show()

c.set_x(100)
print(c.get_x())


