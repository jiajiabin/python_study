import option
import random
#墙
class Wall:
    def __init__(self):
        self.__list = []
    #创建墙的坐标集
    def __init_points(self):
        for i in range(option.size):
            self.__list.append((0,i))
            self.__list.append((option.size - 1,i))
        for i in range(1,option.size-1):
            self.__list.append((i,0))
            self.__list.append((i,option.size-1))
    #返回墙的坐标
    @property
    def points(self):
        self.__init_points()
        return self.__list

class Radblock:
    def __init__(self):
        self.__list = []
        self.init_points()
    #随机生成障碍物
    def init_points(self):
        nums = int((option.size ** 2 ) / 5)
        for i in range(nums):
            x = random.randint(1, option.size - 2)
            y = random.randint(1, option.size - 2)
            if (x,y) in [(2,2),(2,3)]:
                continue
            self.__list.append((x,y))

    # 返回墙的坐标
    @property
    def points(self):
        return self.__list
