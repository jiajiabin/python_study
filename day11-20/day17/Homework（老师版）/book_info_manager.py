import request
import re

class BookInfoManger(request.RequestDelegate):
    def __init__(self):
        self.__request = request.Request(self)
        self.__url = None
        self.__page = ""

    def download(self, url):
        self.__request.request(url)
        self.__url = url
        self.__page = "Book"

    def receive_data(self, data):

        pattern = '<div id="info" class="">(.*)id="interest_sectl"'
        ret = re.search(pattern, data, re.S)

        pattern = '作者(.*)出版社'
        ret = re.search(pattern, ret.group(1), re.S)

        pattern = '<a.*>(.*)</a>'
        ret = re.search(pattern, ret.group(1), re.S)
        ls = ret.group(1).split(" ")
        s = "".join(ls)

        pattern = '<span class="pl">出版社:</span>(.{35})'
        ret = re.search(pattern, data, re.S)
        print(ret.group(1).split("<br/>")[0])

        pattern = '<span class="pl">出版年:</span>(.{35})'
        ret = re.search(pattern, data, re.S)
        print(ret.group(1).split("<br/>")[0])






b = BookInfoManger()
b.download('https://book.douban.com/subject/1432596/')
