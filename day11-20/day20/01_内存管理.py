# python内存管理使用引用机制

# 所有类的父类
class Base:
    def __init__(self):
        self.__ratain_count = 1

    def ratain(self):
        self.__ratain_count += 1
        return self

    def release(self):
        self.__ratain_count -= 1
        if self.__ratain_count == 0:
            self.dealloc()

    # 垃圾回收，销毁对象
    def dealloc(self):
        print("对象被销毁")


b = Base()
c = b.ratain()

print(b)

b.release()

print(c)
c.release()


