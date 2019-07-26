import time
ls = [1, 2, 3, 4, 5]
# 将列表，字典，字符串、集合、元组，均可转换成迭代器
# 凡是能forin遍历的，都能转成迭代器
i = iter(ls)

print(next(i))      # 每次调用next函数，传入迭代器，则返回一个元素
print(next(i))      # 迭代器的元素，next一次，少一个，无法后退

while True:
    time.sleep(1)
    try:
        print(next(i))
    except StopIteration:
        break

# 迭代器已经清空，但是列表没有受到影响
# for in 就是创建迭代器，调用迭代器。



