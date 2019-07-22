# 类方法

class Cube:
    def __init__(self, l, w, h):
        self.__l, self.__w, self.__h = l, w, h

    # 通过类方法创建对象
    @ classmethod
    def standard_cube(cls):                 # cls = Cube
        # cls是Cube类
        return cls(1, 1, 1)


# 类方法，需要用类来调
c = Cube.standard_cube()
# 类方法对于实现“工厂设计模式”更方便

# 类方法和静态方法的区别
# 1.类方法装饰用 @classmethod 静态方法 @staticmethod
# 2.类方法第一个参数是类，如果参数名写为self，这个self指的是类。 静态方法不必传入类名。
# 3.类方法可以通过cls调用其他类方法，静态方法只能通过类名调用类方法
# 4.类方法跟适合实现工厂类
















