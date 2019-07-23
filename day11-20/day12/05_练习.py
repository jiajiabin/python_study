# 写一个长方形的类，拥有长和宽，可以返回面积和周长
# 写一个正方形类，拥有长，可以返回面积和周长，用尽量简单的方式创建这两个类

# class Quad:
#     length = 0
#
#     @property
#     def area(self):
#         return self.length ** 2
#
#
# class Rect(Quad):
#     width = 0
#
#     @property
#     def area(self):
#         return self.length * self.width


class Rect:
    length, width = 0, 0

    @property
    def area(self):
        return self.length * self.width


class Quad(Rect):
    @property
    def length_(self):
        return self.length

    @length_.setter
    def length_(self, l):
        self.length = self.width = l


