# 地铁

# 站类
class Station:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


# 线类
class Line:
    def __init__(self, name):
        self.__list = []
        self.__name = name

    @property
    def name(self):
        return self.__name

    #添加站
    def add(self, index, name):
        self.__list.insert(index, Station(name))

    # 打印线上所有的站
    def __repr__(self):
        s = ""
        for i in self.__list:
            s += i.name + "-"
        return s[:-1]

    # 判断当前线与另一个线是否相交
    def __mul__(self, other):
        for i in self.__list:
            for j in other.__list:
                if i.name == j.name:
                    return True

        return False


# 地铁线路类
class Lines:
    def __init__(self):
        self.__list = []

    # 添加站
    def add(self, station_name, line_name, index):
        # 找到对应的线
        for i in self.__list:
            if i.name == line_name:
                i.add(index, station_name)
                return
        # 如果没有这条线，创建这条线
        line = Line(line_name)
        line.add(0, station_name)

    # 打印一条线上所有的站
    def print_line(self, line_name):
        for i in self.__list:
            if i.name == line_name:
                print(i)
                return

    # 判断两条线是否相交
    def is_inter(self, line_name1, line_name2):
        # 根据名字，找出两条线
        line1, line2 = None, None
        for i in self.__list:
            if i.name == line_name1:
                line1 = i
            elif i.name == line_name2:
                line2 = i

        if line1 == None or line2 == None:
            return False

        return line1 * line2




