# 将一个对象的引用，赋值给一个变量，则该变量也变成了同一个对象的引用
# 一个对象可以有若干引用

# 任何一个对象是无法存储在另一个对象当中的。因此无论是自定义的类还是容器，都不能真正存储其他对象，只是存储了对象的地址
# 因此将对象存入容器，是给对象添加一个引用，从容器中返回对象，则返回对象的地址，如同复制了对象的引用.
# 如果将一个对象添加到多个容器，多个容器访问的是同一个对象。

class Point:
    def __init__(self, x=1, y=2):
        self.__x, self.__y = x, y

    def set_x_y(self, x, y):
        self.__x, self.__y = x, y

    def __repr__(self):
        return "({},{})".format(self.__x, self.__y)


ls1 = [Point(), Point(2, 4), Point(4, 5)]
# 三个引用 ls1[0]   ls1[1]  ls1[2]
p = ls1[1]
# p和ls1[1]是同一个Point对象的引用
p.set_x_y(6, 7)

print(ls1)

ll = [1, 2, 3, 4, 5]
x = ll[1]
x = 6       # 因为这里修改的是x的值，而不是修改x指向的对象
print(ll)








