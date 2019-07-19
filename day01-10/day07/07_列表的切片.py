ls = ["zero", "one", "two", "three", "four", "five"]
# 根据索引，取出单个元素
print(ls[0], ls[1], ls[2])

# 修改单个元素
ls[0] = "123"
ls[1] = "abc"
print(ls)


ls = ["zero", "one", "two", "three", "four", "five"]
# 列表的切片提取
print(ls[1:])
print(ls[:4])
print(ls[1:4])
print(ls[1:4:2])
print(ls[4:1:-1])

print(ls[-1], ls[-2])
print(ls[1:-1])

# 切片可以直接修改列表的内容
ls[2:4] = ["good", "good", "study", "day", "day", "up"]
print(ls)

# 【注】上述切片操作，除了赋值之外，全都是生成一个新的列表，没有修改原列表ls

