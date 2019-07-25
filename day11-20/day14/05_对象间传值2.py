# 郭德纲 给 各种人钱  包括 儿子， 徒弟， 员工

# 所有收钱人的父类
class EverOne:
    # 所有想收钱的子类，都必须继承这父类，重写收钱方法
    def recive_money(self): return 0
    # 继承实现了统一接口，实现多态的作用


class Boss:
    def __init__(self, name):
        self.__name = name
        self.__money = 10000000

    def show_money(self):
        print("%s:%d" % (self.__name, self.__money))

    def send_money(self, one: EverOne):      # 如果函数的形参是父类，也可以子类的对象
        # 委托收钱人钱增长, 返回值是委托人钱增长的数量
        ret = one.recive_money()
        self.__money -= ret


class Son(EverOne):
    def __init__(self, name):
        self.__name = name
        self.__money = 10000000

    def show_money(self):
        print("儿子%s:%d" % (self.__name, self.__money))

    def recive_money(self):
        self.__money += 100000
        return 100000


class Stu(EverOne):
    def __init__(self, name):
        self.__name = name
        self.__money = 10000000

    def show_money(self):
        print("徒弟%s:%d" % (self.__name, self.__money))

    def recive_money(self):
        self.__money += 5000
        return 5000


guodegang = Boss("郭德纲")
yueyunpeng = Stu("岳云鹏")
guodegang.send_money(yueyunpeng)

guodegang.show_money()
yueyunpeng.show_money()