# 字典 dict（dictionary）

d = {"one": 1, "Two": 2, "Three": 3, "Four": 4}
# 字典是一个容器，用于存储和管理数据
# 字典中的数据以键值对的方式存储
# "one" 和 1是一个键值对，其中"one"称为键[key]，1称为值[value]
# 键是不可变数据，值随便
# 键是寻找值的索引，值才是我们存储的数据。
# 字典中每个键是唯一的，不会有两个键值对拥有相同的键，值随意
# 字典中数据没有顺序

# 创建字典
d2 = dict(d)


# 打印字典
print(d)


# 遍历字典
for i in d:
    print(i, d[i])

# 遍历简直对
for i in d.items():
    print(i)
# d.item() 会返回一个列表，列表中是元组，元组中是键和值

# 通过键查找值
print(d["one"], d["Two"])

# 通过键，修改值
d["one"] = [1, 2, 3]
print(d)
print(d["one"][0])

