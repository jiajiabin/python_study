
class Math:
    # 有的时候，我们会编写出用不到成员变量的方法
    # 这时候，self就没有用了
    # 去掉self，装饰一个staticmethod的装饰器
    @staticmethod
    def add(a, b):
        return a + b


# 静态方法既可以用对象的引用调用，也可以用类名直接调用
m = Math()
print(m.add(1, 2), Math.add(1, 2))
# 本质上对象名也好，类名也好，都是为了表明这个函数是属于Math类的函数。
# 其实静态函数和类外的函数是一样的。

# 静态方法的主要用处
# 1.创建对象(类方法)
# 2.留下简洁的对外接口(静态方法)


class Cube:
    def __init__(self, length, width, height):
        self.__length, self.__width, self.__height = length, width, height

    # 创建标准立方体，即长、宽、高均为1的正立方体
    @staticmethod
    def standard_cube():
        return Cube(1, 1, 1)


c = Cube.standard_cube()
