import requestbook
import re
from whiteintxt import WhiteIntxt

class BookInfo(requestbook.RequestDelegate):
    def __init__(self):
        self.__request = requestbook.RequestBook(self)

    def receive_data(self, data):
        self.analyze_data(data)
    def download(self,url):
        self.__request.request(url)
    def analyze_data(self,data):
        whitetxt = WhiteIntxt()
        #获取书名
        pattern1 = '"name" : "(.*)",\n\s*"author":'
        ret1 = re.search(pattern1, data, re.S)
        if ret1 == None:
            return
        whitetxt.set_name(ret1.group(1))
        # 获取作者
        pattern2 = '"@type": "Person",\n\s*"(.*)\n\s*}\n\s*]'
        ret2 = re.search(pattern2, data, re.S)
        ls2 = ret2.group(1).split("{")
        for i in ls2:
            patterni = 'name": "(.*)"'
            ret2i = re.search(patterni, i, re.S)
            whitetxt.set_writer(ret2i.group(1))
        # 获取评分
        pattern3 = '<strong class="ll rating_num " property="v:average"> (.*) </strong>'
        ret3 = re.search(pattern3, data, re.S)
        whitetxt.set_score(ret3.group(1))
        # 获取简介
        pattern4 = '<div class="intro">\n\s*<p>(.*)</div>\n\n\s*</div>\n\s*</span>'
        ret4 = re.search(pattern4, data, re.S)
        ls4 = ret4.group(1).split('<div class="intro">\n')
        ls40 = ls4[-1].split('</p>')
        for i in ls40[:-1]:
            ls41 = i.split('<p>')
            whitetxt.set_introduction(ls41[-1])
        #获取短评
        pattern5 = '<span class="">短评</span>(.*)">全部\s[0-9]*\s条</a>'
        ret5 = re.search(pattern5, data, re.S)
        ls5 = ret5.group(1).split(r'</a>')
        pattern50 = '全部 ([0-9]*) 条'
        ret50 = re.search(pattern50, ls5[0], re.S)
        # 短评数量
        nums1 = ret50.group(1)
        page1 = int(nums1) // 20 + 1
        pattern51 = '<a href="(.*)">全部'
        ret51 = re.search(pattern51, ls5[0], re.S)
        for i in range(page1):       #page1
            url = ret51.group(1)+ "hot?p=" + str(i+1)
            data51 = self.__request.request1(url)
            pattern52 = '<h1>时间的秩序 短评</h1>(.*)我来写短评</a>'
            ret52 = re.search(pattern52, data51, re.S)
            ls6 = ret52.group(1).split("有用")
            ls6 = ls6[1:]
            for j in ls6:
                pattern60 = '<a href="https://www.douban.com/people(.*)/a>\n\s*<span'
                ret60 = re.search(pattern60, j, re.S)
                pattern61 = '>(.*)<'
                ret61 = re.search(pattern61, ret60.group(1), re.S)
                pattern62 = ' <span class="short">(.*)</span>\n\s*</p>\n\s*</div>'
                ret62 = re.search(pattern62, j, re.S)
                whitetxt.set_short_commentary(ret61.group(1),ret62.group(1))
        whitetxt.white()
path = "https://book.douban.com/subject/33424487/?icn=index-topchart-subject"
mim = BookInfo()
mim.download(path)



