# 1.写一个发报机，有一个函数，参数是发送的报文str，将报文发送给任意对象。

# 接收数据的对象的父类
class ReciveDataDelegate:
    def recive_data(self, data): pass
    # 【注】我们可以看到，这个方法实际上是代理方（接收数据方）的方法。是委托方来调用
    # 这个函数的参数，会从委托方传给代理方，这个函数的返回值会从代理方返回到委托方


class Sender:
    def send(self, message, ever_object:ReciveDataDelegate):
        ever_object.recive_data(message)


class Reciver(ReciveDataDelegate):
    def recive_data(self, data):
        for i in range(3):
            print(data)



sender = Sender()
reciver = Reciver()

sender.send("hello world!", reciver)

