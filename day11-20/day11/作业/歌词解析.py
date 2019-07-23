class Sentence:
    def __init__(self, time, word):
        self.__time = time
        self.__word = word

    def get_word(self):
        return self.__word


class Lyric:
    def __init__(self):
        self.__list1 = []
        self.__dict1 = {}

    def set_list(self, time):
        self.__list1.append(time)
        self.__list1.sort()

    def set_dict(self, time, word):
        self.__dict1[time] = Sentence(time, word)

    def read_lyric(self, path):
        file1 = open(path, "r", encoding="UTF-8")
        self.__list1.clear()
        self.__dict1.clear()
        while 1:
            x1 = file1.readlines(1)
            if len(x1) < 1:
                break
            str1 = x1[0]
            list2 = str1.split("]")
            if list2[-1] == "\n":
                continue
            if len(list2) > 2:
                word1 = list2[-1]
                for i in range(len(list2) - 1):
                    time1 = list2[i][1:]
                    time1 = self.time_switch(time1)
                    self.set_list(time1)
                    self.set_dict(time1, word1)
            else:
                word1 = list2[-1]
                time1 = list2[0][1:]
                time1 = self.time_switch(time1)
                self.set_list(time1)
                self.set_dict(time1, word1)
        file1.close()

    def time_switch(self, time):
        time2 = time.split(":")
        return int(time2[0]) * 60 + int(time2[1])

    def return_lyric(self, time):
        time3 = self.time_switch(time)
        if self.__list1[0] > time3:
            return " "
        elif self.__list1[-1] <= time3:
            return self.__dict1[self.__list1[-1]].get_word()
        else:
            for i in range(len(self.__list1)):
                if self.__list1[i] <= time3 and time3 < self.__list1[i + 1]:
                    return self.__dict1[self.__list1[i]].get_word()

    def run(self):
        self.read_lyric("乱世巨星2.lrc")
        while True:
            eng = input("请输入时间:\n")
            print(self.return_lyric(eng))


Lyric().run()
