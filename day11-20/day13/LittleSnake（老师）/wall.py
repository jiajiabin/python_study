import option
# 墙的类，创建围墙
class Wall:
    def __init__(self):
        self.__list = []
        self.__init_points()

    # 创建代表墙的一组坐标
    def __init_points(self):
        for i in range(option.size):
            # 创建第一行
            self.__list.append((0, i))
            # 创建最后一行
            self.__list.append((option.size - 1, i))
            # 创建第一列
            self.__list.append((i, 0))
            # 创建最后一列
            self.__list.append((i, option.size - 1))

    # 返回墙的坐标
    @property
    def points(self):
        return self.__list