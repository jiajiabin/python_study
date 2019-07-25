import time
class Timer:
    # 哪个对象，干什么，时间间隔是多少，是否重复，参数
    def __init__(self, obj, func, stepper, repeat, *arg):
        self.__obj, self.__func, self.__stepper, self.__repeat, self.__arg = obj, func, stepper, repeat, arg

    def __run(self):
        for i in range(self.__repeat):
            time.sleep(self.__stepper)
            self.__func(self.__obj, *self.__arg)
            # Stu.speak_name(xiaoming, "吃香蕉")

    def start(self):
        self.__run()


class Stu:
    def __init__(self, name):
        self.__name = name

    def speak_name(self, favor):
        print("我是{}，我爱{}".format(self.__name, favor))


xiaoming = Stu('王小明')
# 调用定时器，每5秒钟报一次名，共报5次
timer = Timer(xiaoming, Stu.speak_name, 5, 5, "吃香蕉")
timer.start()
