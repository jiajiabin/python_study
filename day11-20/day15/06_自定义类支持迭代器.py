# 英语子母类，从这个类当中，可以取出每一个英语字母
class EnglishCharacter:
    def __init__(self):
        self.__str = "abcdefghijklmnopqrstuvwxyz"
        self.__str += self.__str.upper()
        self.__index = 0

    # 通过[]+索引值返回英文字母
    def __getitem__(self, item):
        # item就是索引，可以是任何不可变数据
        if item == "day":
            return "Monday, Tuesday, Wednesday, Thursday, Friday. Saturday, Sunday"
        return self.__str[item]

    # 如果要生成迭代器，需要[重写]下面两个方法
    def __iter__(self):
        self.__index = 0        # 每次生成迭代器的时候，计数重来
        return self             # 固定返回self

    def __next__(self):         # 返回值是每次调用next，得到的数据
        if self.__index >= len(self.__str):
            raise StopIteration("已经没有字母了")      # 要抛出迭代结束的异常
        value = self.__str[self.__index]
        self.__index += 1
        return value




c = EnglishCharacter()
print(c[0], c[1], c["day"])

i = iter(c)
while True:
    try:
        print(next(i))
    except StopIteration as e:
        print(e)
        break

# 能使用迭代器，就能使用for in
for i in c:
    print(i)    # i就是next的返回值


