# 列表
# 储存、管理大量的数据。

# 创建列表  难  重要
l = [1, 2, 5, 8, "hello world!", 9.0, True]
print(l)

# 通过构造函数（创建列表的函数）创建列表
l = list([1, 2, 3, 4, 6])
print(l)

# 通过序列创建列表
l = list(range(10))
print(l)

l = list(range(1, 10, 2))
print(l)

# 通过【生成式】创建列表
# 在Python中有一种特殊的运算式可以用于灵活的初始化列表，字典，集合等数据，这种运算式称为生成式
# 生成式与一般的python语法，结构不同


l = [i for i in range(1, 10, 2)]
print(l)
l = [i / 2 for i in range(1, 10, 2)]
print(l)
l = [pow(i, 2) for i in range(5)]
print(l)

l = [i for i in range(1, 100) if i % 7 == 0]
print(l)

l = [i ** 2 if i > 5 else i / 2 for i in range(1, 10)]
# i的范围是1到9， 如果i大于5，在列表中加一个i的平方，如果i不大于5，在列表中加一个i / 2
print(l)


# 练习:
#1.创建一个列表，其元素是，半径为1，2，3.。。10的圆的面积
l = [r ** 2 * 3.14 for r in range(1, 11)]
print(l)

#2.在上一题基础上，仅将值大于50的面积 加入列表
l = [r ** 2 * 3.14 for r in range(1, 11) if r ** 2 * 3.14 > 50]
print(l)

#3.遍历1-10所有的数，奇数求立方加入列表，偶数求平方加入列表
l = [r ** 2 if r % 2 == 0 else r ** 3 for r in range(1, 11)]
print(l)











