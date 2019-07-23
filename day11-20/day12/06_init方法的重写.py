# init方法的重写
class Parent:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __repr__(self):
        return "姓名:{}\n年龄:{}\n".format(self.__name, self.__age)


class Child(Parent):
    def __init__(self, name, age, height, weight):
        # 子类的init可以调用父类的init初始化父类的那一部分，然后再初始化子类独有的部分。
        # 【注】如果父类的init方法没有参数，子类是否还需要调用父类的init方法呢
        # 需要。因为父类init很可能做一些不需要传参的初始化。
        super().__init__(name, age)
        self.__height = height
        self.__weight = weight

    def __repr__(self):
        return super().__repr__() + "身高:{}\n体重:{}\n".format(self.__weight, self.__height)


c = Child("张三", 18, 1.68, 62)
print(c)

