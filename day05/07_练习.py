# 4.编写函数，传入梯形的上底、下底和高，返回梯形的面积。


def area(top, bottom, height):
    return (top + bottom) * height / 2

print(area(1, 2, 3))
