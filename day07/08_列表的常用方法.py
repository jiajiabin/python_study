# 列表是一个可变的内置数据结构
# 列表的方法无非增删改查

def create_list():
    return [i for i in "零一二三四五六七八九十"]

ls = create_list()
# 增
# 追加
ls.append("十一")             # 将新元素追加到末尾
print(ls)
# 插入
ls.insert(5, "ABCD")          # 将新元素插入到位置5，插入后，该元素的索引是5，原来第5及以后元素后移1位。
print(ls)
# 导入
ls.extend([1, 2, 3, 4])        # 从另一个列表中导入数据，追加在最后
print(ls)


ls = create_list()
# 删
# 删除任意一个元素，实际上会删除最后一个元素
ls.pop()
print(ls)
# 根据索引，删除指定的元素
ls.pop(4)
print(ls)
ls = create_list()
# 删除指定值的元素
ls.remove("三")
print(ls)
ls = create_list() + ["三"]
print(ls)
ls.remove("三")      # 从左至右，只删除一个
print(ls)
# 删除所有的元素
ls.clear()
print(ls)



# 改
ls = create_list()
ls[2:4] = [1, 2, 3, 4, 5]
# 逆序，和逆序切片不同，是真的将当前列表逆序，而非生成新的列表
ls.reverse()
print(ls)
# 排序 将列表中的数字按照一定规律进行排列
ls = [3, 4, 1, 2, 5]
ls.sort()                   # 从小到大排序
print(ls)
ls = [3, 4, 1, 2, 5]
ls.sort(reverse=True)       # 从大到小排序
print(ls)
ls = ["abc", "cdef", "abcdef", "bbcd", "bc"]
# 自己规定列表排序的原则，我们需要自定义一个函数，这个函数的参数是一个，参数就是列表的元素
# 返回值是比较大小的值，sort函数会比较这个函数的返回值
ls.sort(key=len, reverse=False)
print(ls)

# 自定义列表排序
ls = [i for i in "一三九八六七二四五零"]
print(ls)
# 自定义比较大小的规则
def cmp(s):
    return "零一二三四五六七八九十".find(s)
ls.sort(key=cmp)
print(ls)


ls = create_list()
# 查
print("八" in ls)
print("十一" in ls)

# 查找出现的位置
print(ls.index("八"))
print(ls.index("八", 4, 9))










