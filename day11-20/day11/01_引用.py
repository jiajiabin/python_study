# 在C++中【指针】和【引用】是两个非常不同的概念
# 但是其他面向对象的编程语言中，【引用】就是C++中的【指针】

# 大多面向对象的编程语言，如Python，创建的对象，创建在堆空间，而非函数执行的占空间
# 因此，函数无法找到堆空间的对象，引用是找寻堆空间即找寻对象的，邮局或送信员

class Rect:
    def __int__(self):
        self.length, self.width = 1, 2

    def print_area(self):
        print(self.length * self.width)

# Rect()在堆空间创建了一个对象，返回了对象的地址，我们将地址赋值给r1，r1是一个装数字的变量，它被称为对象的【引用】。
# 引用装了对象的地址，对象占用内存空间的门牌号
r1 = Rect()
# r1不是对象，但是通过r1，可以找到对象可以使用/访问对象
r1.length = 5

r2 = r1
print(r2.length)
r2.length = 10

print(r1.length)

# 在部分语言，比如Objective-C Swift称引用调用函数叫做向对象发消息
r1.print_area()


ls = [r1]
item = ls[0]
item.length = 100
