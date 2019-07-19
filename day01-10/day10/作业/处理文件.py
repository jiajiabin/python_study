class Words:
    def __init__(self, word, translate):
        self.__word = word
        self.__translate = translate

    def set_word(self, word):
        self.__word = word

    def set_translate(self, translate):
        self.__translate = translate

    def get_word(self):
        return self.__word

    def get_translate(self):
        return self.__translate


class Dictionaries:
    def __init__(self):
        self.word_dict = {}

    def store_words(self, word, translate):
        self.word_dict[word] = Words(word, translate)

    def get_wors_translate(self, word):
        if self.word_dict.get(word):
            return self.word_dict[word].get_translate()
        else:
            return "sorry，字典中找不到此单词"


class Manage:
    def __init__(self, file):
        self.__file = file
        self.dict = None

    def get_dict(self):
        self.dict = Dictionaries()

    def close_file(self):
        self.__file.close()

    def manage_file(self):
        x0 = self.__file.readlines(1)
        self.__cut1(x0)
        while 1:
            x1 = self.__file.readlines(1)
            if len(x1) < 1:
                break
            self.__cut2(x1)

    def __cut1(self, list):
        str1 = list[0]
        list1 = str1.split("\t")
        word1 = list1[0]
        word2 = word1[-6] + word1[-5] + word1[-4] + \
                word1[-3] + word1[-2] + word1[-1]
        translate1 = list1[1]
        self.dict.store_words(word=word2, translate=translate1)

    def __cut2(self, list):
        str2 = list[0]
        list2 = str2.split("\t")
        word1 = list2[0]
        translate1 = list2[1]
        if "\\n" in translate1:
            list3 = translate1.split("\\n")
            translate1 = ""
            for i in range(1, len(list3)):
                translate1 += "%d.%s\n" % (i, list3[i - 1])
            translate1 += "%d.%s" % (len(list3), list3[len(list3) - 1])
        self.dict.store_words(word=word1, translate=translate1)


manage = Manage(open("dict.txt", "r", encoding="UTF-8"))
manage.get_dict()
manage.manage_file()
manage.close_file()

print(manage.dict.get_wors_translate("Africa"))
print(manage.dict.get_wors_translate("Arab"))
print(manage.dict.get_wors_translate("zo"))
