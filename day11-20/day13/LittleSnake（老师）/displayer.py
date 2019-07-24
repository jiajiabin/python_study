import option
import os
# 显示管理类，根据坐标，显示一个nxn的矩阵
class Displayer:
    # init方法
    def __init__(self):
        # 装坐标点的列表，列表中都是这样的坐标点(x,y)元组
        self.__list = []

    # 导入需要显示的坐标点数据
    def extend_points(self, point_list):
        self.__list.extend(point_list)

    # 清空这一帧的数据
    def clear(self):
        self.__list.clear()

    # 打印点阵图
    def draw_graphics(self, score):
        os.system("cls")    # 清屏 然后打印
        print("".center(option.size * 2, "="))
        print(("score:%d" % score).center(option.size * 2, " "))
        print("".center(option.size * 2, "="))
        for i in range(option.size):
            for j in range(option.size):
                if (i, j) in self.__list:
                    print("国", end="")
                else:
                    print("  ", end="")
            print()


# d = Displayer()
# d.extend_points([(1, 1), (3, 5), (12, 10), (6, 4)])
# d.draw_graphics()

