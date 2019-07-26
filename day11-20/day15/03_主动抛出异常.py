class Fraction:
    def __init__(self, divised, division):
        # 判断分母为0，抛出异常
        if division == 0:
            # 主动的抛出异常对象
            raise ZeroDivisionError()
        self.__divised, self.__division = divised, division

    # 格式化输出
    def show(self):
        print("{}/{}".format(self.__divised, self.__division))

    # 转成小数
    def to_float(self):
        return self.__divised / self.__division

while True:
    try:
        divised, division = int(input()), int(input())
        f = Fraction(divised, division)     # 一旦try当中的代码抛出了异常，try中的代码就会中断
        break
    except ZeroDivisionError:
        print("输入错误，请重试")

print(f.to_float())
f.show()