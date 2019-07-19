# python可以自定义运算符的功能，有点类似于某些语言具有重载运算符的功能

class Point:
    def __init__(self, x, y):
        self.__x, self.__y = x, y

    def __repr__(self):
        return "({}, {})".format(self.__x, self.__y)

    # 自定义两个Point相加的到一个新的Point对象，新的Point的x是两个point的x的和，y是两个point的y的和
    def __add__(self, other):
        # s1+s2 则加号是个幌子，实际上是调用这个函数，s1就是self s2就是other
        return Point(self.__x + other.__x, self.__y + other.__y)

    # add sub mul
    def __truediv__(self, other):
        return 4

    def __mod__(self, other):
        return 5


p1 = Point(3, 4)
p2 = Point(5, 6)
p3 = Point(7, 0)
p = p1 + p2 + p3

print(p)

print(p1 % p2)


