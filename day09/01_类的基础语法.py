# 类基本创建和使用

# 创建一个类
class Rectangle:
    # 成员变量，也称字段，描述对象的特征
    length, width = 0.0, 0.0

    # 成员函数，也称成员方法，描述对象的行为
    def get_area(self):
        # 成员函数，和写在类外面的函数没有什么本质区别，只是成员函数会自带一个参数，self
        # 成员函数可以通过self，使用成员变量。而无需在函数内声明。
        # 凡是能写在类外函数中的代码，都能写在成员函数中。
        return self.length * self.width

# 类是一个自定义的类型，就像是int，就像str，本身不能存储数据，只有用类型创建的变量，即用类实例化的对象，才能储存数据
# int = 5   a = 5
r = Rectangle()     # Rectangle()是创建了一个矩形对象，然后，赋值给r

# 通过r可以使用成员变量
r.length = 10
r.width = 5
# 创建的矩形对象，拥有内存空间，内涵r.length 和r.width

# 通过r可以使用成员函数
ret = r.get_area()      # self是不用传参的
# 返回值仍然是函数调用表达式的值 r.get_area()的值
print(ret)

# 一个类，可以创建多个对象，如同一个类型可以创建多个变量，但是多个变量是不同的内存空间，一个改变了，跟另一个没有关系
r2 = Rectangle()
r2.length, r2.width = 5, 2

print(r.get_area(), r2.get_area())

print(type(r), type(r2))






