from enum import IntEnum, unique

# IntEnum是一个常用的Enum的子类，要求每个枚举值的值，都是int类型
# unique是一个装饰器，装饰一个Enum子类，让子类当中的枚举值的值不能重复


@unique
class IphoneType(IntEnum):
    IPHONE = 0
    IPHONE3 = 1
    IPHONE4 = 2
    IPHONE4S = 3
    IPHONE5 = 4
    IPHONE5C = 5
    IPHONE5S = 6
    IPHONE6 = 7
    # IPHONE6PLUS = 7

    # 传入若干个版本，返回一个最新的
    @staticmethod
    def find_newest(t, *arg):
        m = t
        for i in arg:
            if i.value > m.value:
                m = i
        return m


t = IphoneType.IPHONE6
t1 = IphoneType.IPHONE5
print(t, t1)

print(IphoneType.find_newest(IphoneType.IPHONE3, IphoneType.IPHONE4S, IphoneType.IPHONE4))


def func():
    return 1, 2, 3

a, b, c = func()
print(a, b, c)


# for i in range(10):
#     pass
# print(i)

import random
print(random.random())

num1 = 5 and -1
print(num1)
num2 = 3 or -9
print(num2)
result = num1*num2 + 3 
print(result)




