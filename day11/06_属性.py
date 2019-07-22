class Rect:
    def __init__(self, l, w):
        # 直接用字母开头的变量，是【公有变量public】
        # 通过两个下划线开头的变量，是【私有变量private】
        # 建议使用私有变量，拥有赋值更易管理性。但是使用没有那么方便
        self.__length = l
        self.__width = w

    def set_length(self, l):
        if l >= 0:
            self.__length = l
        else:
            self.__length = 0

    # 通过装饰器可以将get方法装饰城属性
    @property
    def width(self):
        return self.__width

    @width.setter           # 可以有getter没有setter，不能只有setter  setter 即set方法  getter即get方法
    def width(self, w):
        self.__width = w

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, l):
        print("!@#")
        if l >= 0:
            self.__length = l
        else:
            self.__length = 0

r = Rect(1, 2)
r.set_length(5)
r.width = 10        # 声明为属性之后，就可以用点来调用。仅支持一个参数
print(r.width)

r.length = 10       # 通过赋值运算符赋值，既是调用setter方法
print(r.length)     # 通过点运算符取值，既是调用getter方法

