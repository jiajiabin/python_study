class MyIter:
    def __init__(self, object = None):
        self.__object = object

    @property
    def obj(self):
        return self.__object

    def iter(self):
        return None
    def next(self):
        return None


def my_iter(object: MyIter):
    i = MyIter(object.iter())
    return i

def my_next(i:MyIter):
    return i.obj.next()


class EnglishCharacter(MyIter):
    def __init__(self):
        super().__init__()
        self.__str = "abcdefghijklmnopqrstuvwxyz"
        self.__str += self.__str.upper()
        self.__index = 0

    def iter(self):
        return self

    def next(self):
        if self.__index >= len(self.__str):
            raise StopIteration("已经没有字母了")      # 要抛出迭代结束的异常
        value = self.__str[self.__index]
        self.__index += 1
        return value


c = EnglishCharacter()
i = my_iter(c)
while True:
    try:
        print(my_next(i))
    except StopIteration as e:
        print(e)
        break