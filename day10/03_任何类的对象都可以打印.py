# 官方类，number、str、tuple、list、dict、set都是可以通过print进行打印的
# 其实，任何类的对象都可以通过print来打印。

class Rect:
    def __init__(self, length, width):
        self.__length, self.__width = length, width

    def set_length_width(s, l, w):
        s.__length, s.__width = l, w

    def get_area(self):
        return self.__length * self.__width

    # 按照自身需求，自定义print打印的内容
    def __repr__(self):
        # 函数名字就像init一样是固定的，不可修改的
        # 打印当前类的对象，就是打印这个函数的返回值
        return "矩形:(长为{}，宽为{}，面积为{})".format(self.__length, self.__width, self.get_area())

    # 除了打印，只要实现了下列方法，任何类的对象，都能强转成字符串
    def __str__(self):
        # 强转当前对象为字符串，得到就是这个函数的返回值
        return "矩形:(长为{}，宽为{}，面积为{})".format(self.__length, self.__width, self.get_area())

    # 对象可以转成任意的number类型
    def __int__(self):
        return 5
    def __float__(self):
        return 1.5


r = Rect(3, 4)
print(r)

s = str(r)
print(s)

print(int(r))