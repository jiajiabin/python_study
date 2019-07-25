from request import Request
from request import RequestDelegate
import time

class Data:
    pass


# 数据管理模块，下载并管理数据
class DataManager(Data, RequestDelegate):
    def __init__(self):
        self.__request = Request()

    # 下载数据
    def download_data(self):
        self.__request.request_data(self)

    # DataManager就是接收数据的一方，继承RequestDelegate，重写了方法
    def receive_data(self, data):
        # 调用这个函数是为了回传下载到的数据，所以这个函数，一般叫做【回调函数】
        # 调用这个函数的过程，则称为【回调】
        print("收到数据", data)
        print("解析数据!!")


data_manager = DataManager()
data_manager.download_data()

while True:
    time.sleep(0.8)
    print("主线程工作中...")
