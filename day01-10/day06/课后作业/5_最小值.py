# 4.将获得最小值的方法 的内部实现 使用自己的代码完成
def min_self(*args):
    for i in args:
        min = i
        break
    for i in args:
        if min > i :
            min = i
    print(min)

min_self(4,2,3,4,5,6)