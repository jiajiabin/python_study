class WhiteIntxt:
    def __init__(self):
        self.__name = None
        self.__writer = []
        self.__score = 0
        self.__introduction = []
        self.__short_commentary = {}
    # 书名
    def set_name(self, name):
        self.__name = name
    # 作者
    def set_writer(self, writer):
        self.__writer.append(writer)
    # 评分
    def set_score(self, score):
        self.__score = score
    # 简介
    def set_introduction(self, introduction):
        self.__introduction.append(introduction)
    # 短评
    def set_short_commentary(self, name,short_commentary):
        self.__short_commentary[name] = short_commentary
    def white(self):
        path = r"bookmessage1.txt"
        file = open(path, "w", encoding="utf-8")
        file.write("书名：")
        file.write(self.__name)
        file.write("\n")
        file.write("作者：")
        for i in self.__writer:
            file.write(i)
            file.write("\t")
        file.write("\n")
        file.write("评分：")
        file.write(self.__score)
        file.write("\n")
        file.write("简介：")
        file.write("\n")
        for i in self.__introduction:
            file.write(i)
            file.write("\n")
        file.write("短评：")
        file.write("\n")
        for i,v in self.__short_commentary.items():
            file.write(i)
            file.write("：")
            file.write(v)
            file.write("\n")
            file.write("\n")