# 所谓对象间传值，就是一个对象，将数据发送给另一个对象。

# 郭德纲 交给 郭麒麟 10,0000

# 父类：财产（字段） 给钱/公开钱(方法) 子类：财产(字段) 收钱/公开钱(方法)
# 【思考】儿子的财产，是儿子自己的字段，因此只有儿子的方法可以修改这个字段。
# 因此，应该是儿子收钱的方法，修改了钱数
# 父类发送给儿子钱的时候，我们可以认为父亲【委托】了儿子的钱增长。

class Son:
    def __init__(self, name):
        self.__name = name
        self.__money = 0

    def show_money(self):
        print("%s:%d" % (self.__name, self.__money))

    def money_rise(self, num):
        self.__money += num


class Father:
    def __init__(self, name):
        self.__money = 1000000
        self.__name = name

    def show_money(self):
        print("%s:%d" % (self.__name, self.__money))

    def send_money(self, son: Son):
        self.__money -= 100000
        # 郭德纲调用郭麒麟的方法，增长了郭麒麟的钱，我们认为是郭德纲【委托】郭麒麟的钱增长。
        # 称郭麒麟是郭德纲的【代理】
        # 这个设计模式就叫做【代理】也叫做【委托代理】
        son.money_rise(100000)


guodegang = Father("郭德纲")
guoqilin = Son("郭麒麟")
guodegang.show_money()
guoqilin.show_money()

guodegang.send_money(guoqilin)

guodegang.show_money()
guoqilin.show_money()



