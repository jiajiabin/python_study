# 1.声明一个函数, 可以接受任意个参数, 获得这些数据中的质数
def question01(*a):
    ls = []
    for i in a:
        if i == 2:
            ls += [i]
        for j in (2, i):
            if i % j == 0:
                break
        if j == i:
            ls += [i]
    return ls

print(question01(3, 5, 10, 8, 7))

#
# 2.封装函数 并且写出其对应的匿名函数简化
# 	a. 将小写字母转化为大写字母  [不用考虑传入其他符号]
# 	b. 获得两个数中的最值



#
# 3.书写装饰器: 装饰器功能是
# 	使一个函数只被执行1次  之后再执行结果返回为None
#
# 	例如
# 		def add(a, b):
# 		    return a + b
# 		第一次运行有结果
# 			res = add(12, 22) ====> 34
# 		之后再运行
# 			res = add(12, 22)  ====>None
#
def once(function):
    result = True
    # print("Once!")
    def do_once(*a, **b):
        nonlocal function, result
        if result:
            ret = function(*a, **b)
            result = False
            return ret
        else:
            return None         # None其实就是0 None表示没有值，一个变量没有值，可以设为None，但是Number变量没有值，不能设为None
    return do_once


@once
def add(a, b):
    return a + b


print(add(1, 2))
print(add(3, 4))


# once(add)(1, 2)


# x = once(add)
# x(1, 2)
# # 只有第一次执行add函数会执行这两部
# x(3,4)


# 4.将获得最小值的方法 的内部实现 使用自己的代码完成
def min(*a):
    _m = a[0]
    for i in a:
        if i < _m:
            _m = i
    return _m

