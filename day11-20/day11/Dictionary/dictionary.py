# 找对象 字典(给他英文，返回中文) 属性 词条
# 词条 属性 英文+中文释义

# 词条的类
class Word:
    def __init__(self, eng, chn):
        self.__eng = eng
        self.__chn = self.__repair_chn(chn)

    def __repair_chn(self, chn):
        # 多于一个释义，修正下
        chn_list = chn.split("\\n")
        if len(chn_list) > 1:
            c = ""
            for i in range(len(chn_list)):
                c += "%d.%s\n" % (i + 1, chn_list[i])
            chn = c[:-1]
        return chn

    def get_eng(self):
        return self.__eng

    def get_chinese(self):
        return self.__chn


# 字典类，用于根据英文，查找返回中文
class Dictionary:
    # 管理大量词条
    def __init__(self):
        self.__list = []
        self.__read_analyze()

    # 读取文件添加词条
    def __read_analyze(self):
        file = open("dict.txt", "r", encoding="UTF-8")
        words_list = file.readlines()

        # 解析列表中内容
        self.__analyze_list(words_list)

    # 解析列表内容
    def __analyze_list(self, words_list):
        for i in words_list:        # i是每一行数据 Britain	n. 英国
            if len(i) == 0:
                continue
            # 解析这一行信息，找出中文和英文，创建词条对象
            self.__analyze_line(i)

    # 解析这一行的数据'
    def __analyze_line(self, line):
        ls = line.split("\t")
        word = Word(ls[0], ls[-1])
        self.__list.append(word)

    # 根据英文，查找中文:
    def translate(self, eng):
        for i in self.__list:
            if i.get_eng().lower() == eng.lower():
                return i.get_chinese()
        return "查无此词\n"

    # 启动函数
    def run(self):
        while True:
            eng = input("请输入单词:\n")
            print(self.translate(eng))


# 使用尽量简单
Dictionary().run()







