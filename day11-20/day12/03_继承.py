class Parent:
    def __init__(self):
        # 父类拥有三个字段
        self.a, self.b, self.__c = 0, 0, 0

    # 父类拥有一对儿属性
    @property
    def c(self):
        return self.__c

    @ c.setter
    def c(self, c):
        self.__c = c

    # 父类拥有一个方法
    def print(self):
        print(self.a, self.b, self.c)


class Child(Parent):
    # 子类可以获得父类的属性字段和方法
    # 子类还可以添加自己的字段属性和方法
    d = 0

    def do_sth(self):
        print(self.a, self.b, self.c)


child = Child()
child.a = 10
child.b = 11
child.c = 12
child.d = 13
child.print()
child.do_sth()
