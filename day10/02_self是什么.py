class Rect:
    def __init__(self, length, width):
        self.__length, self.__width = length, width

    def set_length_width(s, l, w):
        s.__length, s.__width = l, w

    def get_area(self):
        return self.__length * self.__width


# 其实声明在类里面的这些成员函数，和声明在外面的成员函数没有甚区别
# self就是调用函数的对象，是装载数据的对象。
# 调用函数的对象，是这个函数的第一个参数。

r = Rect(5, 3)
r.set_length_width(4, 2)
# 其实这个函数是这个样子的set_length_width(r, 4, 2)
print(r.get_area())

Rect.set_length_width(r, 6, 3)
print(Rect.get_area(r))


