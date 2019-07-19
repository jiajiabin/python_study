# 2.封装函数 并且写出其对应的匿名函数简化
# 	b. 获得两个数中的最值
def zui(a, b):
    min1 = min(a, b)
    max1 = max(a, b)
    print("最大值是", max1)
    print("最小值是", min1)


zui(1, 2)

m = 1
n = 2
x = lambda a, b: print("最大值是", max(a, b), "最小值是", min(a, b))
x(m, n)
