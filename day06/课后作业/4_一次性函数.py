"""
3.书写装饰器: 装饰器功能是
使一个函数只被执行1次  之后再执行结果返回为None
例如
    def add(a, b):
        return a + b
    第一次运行有结果
        res = add(12, 22) ====> 34
    之后再运行
        res = add(12, 22)  ====>None
"""


def one_off(function):
    def with_in(*a, **b):
        nonlocal function
        if function not in list1:
            list1.append(function)
            ret = function(*a, **b)
            return ret
        else:
            return "None"

    return with_in


@one_off
def add(a, b):
    return a + b


while 1:
    list1 = []
    a = input("yes or no :")
    if a == "yes":
        print(add(1, 2))
    else:
        break
