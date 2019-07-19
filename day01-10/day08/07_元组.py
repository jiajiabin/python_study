# 元组基本上就是一个不可变的列表
# 元组的目的大多时间不是为了存储大量的数据
# 而是为了将一些意义相关的数据，组合成一个整体

t = (1, 2, 3, 4, 5, "hello world!")
print(t)
print(t[0], t[1], t[2])
print(len(t))

for i in range(len(t)):
    print(t[i])

for i in t:
    print(t)

# 比如带图像界面的程序往往需要用到坐标
# 2d有一个横坐标和一个纵坐标
p1 = (123, 457)
p2 = ("红桃", "A")
stus = {
    "D001": ("张三", 15, 1.54, 71),
    "D002": ("李四", 16, 1.66, 75)
}
# ("192.168.53.170", 7812)

# 元组可以给多个变量赋值
a, b = (1, 2)
print(a, b)


# python是很少见的函数可以返回多个返回值的编程语言
def get_more_retrurn_value():
    return ("192.168.53.170", 7812)


ip, port = get_more_retrurn_value()
print("ip[%s] port[%s]" % (ip, port))



# 额外，通过元组可以用生成式，生成字典
# 经典题目交换字典的键和值
d = {"One": 1, "Two": 2, "Tree": 3}

d = {v: k for k, v in d.items()}
print(d)



