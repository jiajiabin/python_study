import request
import re
from movieInfo import MovieInfoModel


# 下载并解析存储电影信息的类
class MovieInfoManager(request.RequestDelegate):
    def __init__(self):
        self.__request = request.Request(self)

    # 下载数据
    def download(self, url):
        self.__request.request(url)

    # 重写方法接收数据
    def receive_data(self, data):
        # 解析数据
        self.analyze_data(data)

    # 解析html文件
    def analyze_data(self, data):
        # 创建电影信息类
        info = MovieInfoModel()

        # 获取电影名字
        pattern = '"name":(.*)"director":'
        ret = re.search(pattern, data, re.S)
        # 判断是否有内容
        if ret == None:
            return
        pattern = '"(.*)",.*"url"'
        ret = re.search(pattern, ret.group(1), re.S)
        # 存储电影的名字
        info.set_name(ret.group(1))

        # 获取电影的导演
        pattern = '"director":(.*)"author":'
        ret = re.search(pattern, data, re.S)

        # 分割字符串
        ls = ret.group(1).split("}")
        for i in ls[:-1]:
            pattern = '"name": "(.*)"'
            ret = re.search(pattern, i, re.S)
            # 添加一名导演
            info.add_director(ret.group(1))

        # 查找编剧
        pattern = '"author":(.*)"actor":'
        ret = re.search(pattern, data, re.S)

        ls = ret.group(1).split("}")
        for i in ls[:-1]:
            pattern = '"name": "(.*)"'
            ret = re.search(pattern, i, re.S)
            info.add_author(ret.group(1))


        # 查找主演
        pattern = '"actor":(.*)"datePublished"'
        ret = re.search(pattern, data, re.S)

        ls = ret.group(1).split("}")
        for i in ls[:-1]:
            pattern = '"name": "(.*)"'
            ret = re.search(pattern, i, re.S)
            info.add_actor(ret.group(1))

        # 评分
        pattern = '"ratingValue": "(.*)"'
        ret = re.search(pattern, data)
        info.set_score(ret.group(1))

        print(info)




# path = "https://movie.douban.com/subject/26336778/"
# mim = MovieInfoManager()
# mim.download(path)

path = "https://movie.douban.com/subject/"
for i in range(26184578,26184590):
    path = "https://movie.douban.com/subject/"
    path = path + str(i)+"/"
    print(path)
    mim = MovieInfoManager()
    mim.download(path)


"""
作业:
1.抓取豆瓣上书籍的信息
2.同时抓取同一本书的短评列表
3.把抓到的信息存储到一个文件里

4.判断一个输入的邮箱是正确的邮箱。支持（qq，163，126，gmail）
5.同题4，支持任何邮箱
"""


