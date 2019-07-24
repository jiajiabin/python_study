import option
import os

#显示管理
class Displayer:
    def __init__(self):
        #墙壁坐标点列表
        self.__list = []
    #导入显示的坐标点数据
    def extend_points(self,point_list):
        self.__list.extend(point_list)
    #清空数据
    def clear(self):
        self.__list.clear()
    #打印点阵图
    def draw_graphics(self,score,snake_points,bug_point):
        #清屏
        os.system("cls")
        print("".center(option.size * 2, "="))
        print(("score:%d" % score).center(option.size * 2, " "))
        print("".center(option.size * 2, "="))
        for i in range(option.size):
            for j in range(option.size):
                if (i,j) in self.__list:
                    print("田",end="")
                elif (i,j) in snake_points:
                    print("○",end="")
                elif (i,j) in bug_point:
                    print("※",end="")
                else:
                    print("  ",end="")
            print()

# d = Displayer()
# d.extend_points([(1,30),(1,31),(2,31),(2,30)])
# d.draw_graphics()