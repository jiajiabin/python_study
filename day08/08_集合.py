# 集合set
s = {1, 2, 3, 4, 5}
# 集合中的数据每一个都是唯一的
# 集合中的数据没有顺序
# 找出集合中元素没有意义
# 集合虽然也被称为容器，但是其目的不是储存和管理数据的
# 集合表示一个范围，用来判断一个数据是否从属于一个范围，因而对数据进行分类
print(s)

# 创建集合
s = set("abcdefga")
print(s)
s = set(["123", "456", "789"])
print(s)
s = set((1, 2, 4))
print(s)

# 遍历一个集合
for i in s:
    print(i)

# 判断一个数据是否属于集合
print(1 in s)
print(3 in s)

# 集合中添加元素
s.add(5)
print(s)
# 随机删除元素
s.pop()
print(s)
# 删除指定元素
s.remove(4)
print(s)
# 清空
s.clear()
print(s)
