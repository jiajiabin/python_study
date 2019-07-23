class Rect:
    def __init__(self, length, width):
        self.__length, self.__width = length, width
    # 在其他语言中，这个就是构造函数，构造函数不是构造对象的函数，而是初始化的函数。
    # 在C++当中构造函数和类名相同的，在Python不认为这个函数是构造函数，构造函数是new。init就是初始化函数

    def set_length_width(self, l, w):
        self.__length, self.__width = l, w

    def __repr__(self):
        return "({}:{})".format(self.__length, self.__width)

    # 拷贝构造函数就是传参是另一个当前类对象的init函数。
    def copy(self):
        # 创建一个Rect对象，其值和当前对象一样
        return Rect(self.__length, self.__width)


r1 = Rect(3, 4)
r2 = r1.copy()
print(r2)

r2.set_length_width(5, 6)
print(r1, r2)


# 我们所有内置数据结构，除Number外都是对象。
ls = [1, 2, 3, 4]
n_ls = ls
# ls 和 n_ls是同一个列表
n_ls[3] = 18
print(ls, n_ls)         # 仅仅是引用的复制

new_ls = ls.copy()
new_ls[0] = -1
print(ls, new_ls)       # 浅拷贝


# 列表中拥有三个对象
ls = [Rect(1, 2), Rect(3, 4), Rect(5, 6)]
ls2 = ls            # 同一个列表
ls2[0].set_length_width(9, 10)
print(ls, ls2)

ls3 = ls.copy()     # 不同的列表，但是列表中是同一个对象的引用
ls3[0].set_length_width(-1, -1)
print(ls, ls3)

# 浅拷贝指挥拷贝列表对象，但是列表中的其他对象，仍然只有一个。
# 深拷贝则不仅拷贝最外层的对象，连同子对象，子子对象，一起复制。


ls = [1, 2, 3, 4]           # 不是引用，是数值
ls1 = ls
ls1[0] = -1
print(ls, ls1)

ls2 = ls.copy()
ls2[0] = -2
print(ls, ls2)

# 列表里如果是Number值，复制列表，值也就复制了两个.如果列表里是引用，复制列表，引用复制为两个。



# 例题
# ls = [1, 2, 3, 4, [4, 5]]
# ls1 = ls
# ls1[0] = -1
# ls1[4][0] = -2
# print(ls, ls1)

ls = [1, 2, 3, 4, [4, 5]]
ls1 = ls.copy()
ls1[0] = -1             # ls1[0]是个值，复制了就和ls[0]没关系
ls1[4][0] = -2          # ls1[4]是个引用，复制了则ls1[4]和ls[4]是同一个对象的两个引用
print(ls, ls1)






