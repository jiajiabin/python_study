import threading
import time
import random

# 所有接收数据的类的父类
class RequestDelegate:
# 子类必须继承该类，重写下面方法
    def receive_data(self, data): pass

# 下载类，负责下载数据
class Request(threading.Thread):
    def __init__(self):
        super().__init__()
        self.__delegate = None      # 代理对象的引用

    # 数据请求函数
    def request_data(self, delegate: RequestDelegate):
        self.start()    # 开始下载
        self.__delegate = delegate

    def run(self):
        for i in range(random.randint(15, 30)):
           time.sleep(1)
           print("下载中...")
           # 模拟下载的耗时操作

        # 下载到的数据
        data = "我是下载到的数据"
        # 现有数据Data，但是发送给谁呢，发送给未知的对象。
        self.__delegate.receive_data(data)


