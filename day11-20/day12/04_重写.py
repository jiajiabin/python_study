class Parent:
    a, b, c = 0, 0, 0

    def sum(self):
        return self.a + self.b + self.c


class Child(Parent):
    d = 0

    # 当父类的方法不适合子类，子类可以写一个同名的方法，覆盖父类的方法
    # 这个过程叫做重写
    # def sum(self):
        # return self.a + self.b + self.c + self.d
    # 实际工作中，父类的方法虽然不适合子类，未必没有价值，子类不一定要完全重写父类的方法，可以通过super()函数，调用父类的同名方法
    # 完成一部分操作。子类的结果是依托于父类同名函数运算结果，迭代出来的。
    def sum(self):
        return super().sum() + self.d

c = Child()
c.a, c.b, c.c, c.d = 1, 2, 3, 4
print(c.sum())
