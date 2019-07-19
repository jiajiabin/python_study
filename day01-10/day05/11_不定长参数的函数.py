# 写一个函数，求若干数字的和
def add(*a):    # a是一个元组
    s = 0
    for i in a:
        s += i
    return s


print(add(1, 2, 3))




# 形参a是python中六个数据结构中最简单的一个，称为元组，元组非常类似于列表，但是元组的元素不可改变
ls = [1, 2, 3, 4, 5]
ls[2] = "T"
print(ls[0], ls[1], ls[2])

t = (1, 2, 3, 4, "T")
print(t[0], t[1], t[2], t[3], t[4])

# 对于元组，可以通过如下方式，访问所有元素
for i in t:
    print(i)

