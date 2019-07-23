class Parent:
    def __init__(self, name, age):
        # 变量名或函数名是__开头的为【私有变量/函数】即不能被类外部调用，也不能被子类使用的变量或函数
        # 父类的私有变量只能通过父类提供的方法来间接访问
        self.__name = name
        # 变量名或函数名是_开头的为【保护变量/函数】不能在类外被调用，但是能被子类直接访问
        self._age = age
        # 变量名不以_ __开头的是【公有变量/函数】在子类和外部都能直接使用

    @property
    def name(self):
        return self.__name

    def __repr__(self):
        return "姓名:{}\n年龄:{}\n".format(self.__name, self._age)


class Child(Parent):
    def __init__(self, name, age, height, weight):
        super().__init__(name, age)
        self.__height = height
        self.__weight = weight

    def __repr__(self):
        return super().__repr__() + "身高:{}\n体重:{}\n".format(self.__weight, self.__height)

    def do_sth(self):
        print(self.name)
        print(self._age)



c = Child("张三", 15, 1.69, 63)
print(c)
c.do_sth()