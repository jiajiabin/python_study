import time
import os


# 歌词类，其对象存储单句歌词，歌词信息包括“时间”和“词句”
class Lrc:
    def __init__(self, time, words):
        self.__seconds = self.__time_to_seconds(time)
        self.__words = words

    # 时间转秒数
    @staticmethod
    def __time_to_seconds(time):
        # 05:12
        ls = time.split(":")
        return int(ls[0]) * 60 + int(ls[1])

    # 返回时间
    @property
    def seconds(self):
        return self.__seconds

    # 返回词句
    @property
    def words(self):
        return self.__words

    # 返回lrc时间的
    def get_lrc_time(self):
        return self.seconds


# 歌词解析类，管理每一句歌词
class LrcAnalyzer:
    def __init__(self):
        self.__list = []

    # 解析某一个歌词文件
    def analyze_lrc_file(self, file_path):
        # 打开文件，读取文件
        lines = self.__open_read_file(file_path)
        # 解析读取到的列表
        self.__analyze_list(lines)
        # 对歌词进行排序
        self.__sort()

    # 打开读取文件
    @staticmethod
    def __open_read_file(path):
        file = open(path, "r", encoding="UTF-8")
        return file.readlines()

    # 解析列表
    def __analyze_list(self, lines):
        # 清空列表
        self.__list.clear()
        for i in lines:
            # 解析行数据
            self.__analyze_line(i)

    # 解析一行的数据
    def __analyze_line(self, line):
        # [by:毛毛祥]   [00:03]陈小春   [00:22][01:23]叱吒风云 我任意闯万众仰望
        # ] 分割
        sg = line.split("]")
        # 判断第一段是否是时间
        if sg[0][1:2] not in "0123456789":
            return
        for i in sg[:-1]:
            # 创建歌词对象
            lrc = Lrc(i[1:], sg[-1])
            self.__list.append(lrc)

    # 按照时间排序
    def __sort(self):
        self.__list.sort(key=Lrc.get_lrc_time, reverse=True)

    # 传入时间，返回对应歌词
    def words_for_time(self, seconds):
        # 从大到小，根据时间查找,发现的第一个比输入时间小的语句，就是需要显示的。
        for i in self.__list:
            if i.seconds < seconds:
                return i.words
        return ""


lrc_analyzer = LrcAnalyzer()
lrc_analyzer.analyze_lrc_file("乱世巨星2.lrc")
seconds = 0
while True:
    time.sleep(1)
    os.system("cls")        # 系统的清屏命令
    print(lrc_analyzer.words_for_time(seconds))
    seconds += 1




