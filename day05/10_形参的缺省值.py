def area_rect(length=2, width=1):
    return length * width


print(area_rect())          # 不传参，使用缺省值
print(area_rect(5))         # 传一个参，默认给第一个形参赋值，后面的用缺省值
print(area_rect(width=6))   # 键值对传参，没传的用缺省值
print(area_rect(5, 6))


"""
def p(a, b, c, d):
    print(a, b, c, d)
给这个函数添加缺省值,下面只看声明部分，省略函数体
def p(a, b=1, c=2, d=3):    正确
def p(a, b, c=2, d=3):      正确
def p(a, b, c, d=3):        正确
def p(a=1, b, c=2, d=3):    错误
def p(a=0, b=1, c, d=3):    错误

结论:函数的缺省值不必给每一个参数都添加。添加原则是，右侧的参数有缺省值，左侧的可以没有缺省值；右侧的参数如果没有缺省值，左侧不可以有
缺省值
"""


def p(a, b=1, c=2, d=3):
    print(a, b, c, d)


p(3)
p(3, 4)
p(3, 4, 5)

