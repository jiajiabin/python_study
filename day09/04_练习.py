# 1.创建一个立方体的类，字段包括，长、宽、高。编写成员函数，一个返回表面积，一个返回体积。

class Cube:
    def __init__(self, length, width, height):
        self.length, self.width, self.height = length, width, height

    def get_area(self):
        return (self.length * self.width + self.length * self.height + self.width * self.height) * 2

    def get_volume(self):
        return self.length * self.height * self.width


c = Cube(5, 3, 4)
print(c.get_area(), c.get_volume())

# 2.创建一个圆的类，拥有字段，半径，通过init方法设置半径，通过set方法修改半径，并编写函数，返回圆的周长和面积
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, radius):
        self.radius = radius

    def get_perimeter(self):
        return self.radius * 3.14 * 2

    def get_area(self):
        return self.radius ** 2 * 3.14

















