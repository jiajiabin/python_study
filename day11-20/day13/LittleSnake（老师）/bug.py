import option
import random
# 虫子类
class Bug:
    def __init__(self, points):
        self.__point = None
        self.quickly_move(points)

    # 返回虫子占用的坐标
    @property
    def point(self):
        return [self.__point]

    # 随机生成一个坐标
    def quickly_move(self, points: list):
        while True:
        # 随机生成一个虫子的坐标
            row = random.randint(1, option.size - 3)
            col = random.randint(1, option.size - 3)
            if (row, col) not in points:
                break
        self.__point = (row, col)

