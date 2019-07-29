# 下载模块
import requests
import threading


class RequestDelegate:
    def receive_data(self, data): pass


# 数据下载类
class RequestBook(threading.Thread):
    def __init__(self, delegate: RequestDelegate):
        super().__init__()
        self.__delegate = delegate
        self.__url = None
    def request(self, url):
        self.__url = url
        self.start()
    def run(self):
        ret = requests.get(self.__url)
        data = ret.content.decode("utf-8")
        self.__delegate.receive_data(data)
    def request1(self, url):
        ret = requests.get(url)
        data = ret.content.decode("utf-8")
        return data