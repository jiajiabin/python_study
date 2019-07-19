class Trapezoid:
    # top, bottom, height = 0.0, 0.0, 0.0

    # 初始化方法，直接创建一个带具体值的对象
    def __init__(self, top, bottom, height):
        # 在init方法给成员变量赋值，如果没有这个变量，会自动添加
        self.top, self.bottom, self.height = top, bottom, height

    def get_area(self):
        return (self.top + self.bottom) * self.height / 2

    def set_top_bottom_height(self, top, bottom, height):
        self.top, self.bottom, self.height = top, bottom, height


# t1 = Trapezoid()          # 创建对象，必须传入三个参数

t = Trapezoid(4, 5, 6)      # 创建对象时直接传参，实际是在调用init方法
print(t.get_area())

t.set_top_bottom_height(5, 6, 7)
                            # 虽然创建即有值，还可以修改
print(t.get_area())