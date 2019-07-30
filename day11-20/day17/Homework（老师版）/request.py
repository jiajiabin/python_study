# 下载模块
import requests
import threading


class RequestDelegate:
    def receive_data(self, data): pass


# 数据下载类
class Request(threading.Thread):
    def __init__(self, delegate: RequestDelegate):
        super().__init__()
        self.__delegate = delegate      # 记录接收数据的对象
        self.__url = None

    def request(self, url):
        self.__url = url
        self.start()

    def run(self):
        ret = requests.get(self.__url)
        # 得到数据data
        data = ret.content.decode("utf-8")
        # 回传数据
        self.__delegate.receive_data(data)




