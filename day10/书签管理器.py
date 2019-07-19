class URLItem:
    def __init__(self, title, url, stars):
        self.__title = title
        self.__url = url
        self.__stars = stars
        self.__visits = 0
    def set_title(self, title):
        self.__title = title
    def set_url(self, url):
        self.__url = url
    def set_stars(self, stars):
        if stars < 1:
            self.__stars = 1
        elif stars > 5:
            self.__stars = 5
        else:
            self.__stars = stars
    def get_title(self):
        return self.__title
    def get_url(self):
        return self.__url
    def get_stars(self):
        return self.__stars
    def show(self):
        print("".center(30,"="))
        print("标题：{}\n网址：{}\n星级：{}\n访问次数：{}"
              .format(self.__title,self.__url,"*"*self.__stars,self.__visits))

class URLManager:
    def __init__(self):
        self.__list = []
    def __find_urlitem(self,title):
        for i in self.__list:
            if i.get_title() == title:
                return i
        return None
    def add_url(self,title:str,url:str,stars:int):
        item = self.__find_urlitem(title)
        if item != None:
            print("标题为“{}”的书签已存在，添加失败".format(title))
            return
        item = URLItem(title,url,stars)
        self.__list.append(item)
        print("书签“{}”已添加成功".format(title))
    def remove_url(self,title):
        item = self.__find_urlitem(title)
        if not item:
            print("标题为“{}”的书签不存在，删除失败".format(title))
            return
        else:
            self.__list.remove(item)
            print("标题为“{}”的书签删除成功".format(title))
    def change_item(self,title,new_title):
        item = self.__find_urlitem(title)
        if not item:
            print("标题为“{}”的书签不存在，修改失败".format(title))
            return
        else:
            item.self.__title = new_title
            print("书签修改成功")
    def change_url(self,title,new_url):
        item = self.__find_urlitem(title)
        if not item:
            print("标题为“{}”的书签不存在，修改失败".format(title))
            return
        else:
            item.self.__url = new_url
            print("书签修改成功")
    def change_stars(self,title,new_stars):
        item = self.__find_urlitem(title)
        if not item:
            print("标题为“{}”的书签不存在，修改失败".format(title))
            return
        else:
            item.self.__stars = new_stars
            print("书签修改成功")
    def sorting_visits(self):
        n_ls = []
        for i in self.__list:
            for j in range(0, len(n_ls) + 1):
                if j == len(n_ls) or n_ls[j].get_visits() > i.get_visits():
                    n_ls.insert(j, i)
                    break
        for i in n_ls:
            i.show()
    def sorting_stars(self):
        n_ls = []
        for i in self.__list:
            for j in range(0, len(n_ls) + 1):
                if j == len(n_ls) or n_ls[j].get_stars() > i.get_stars():
                    n_ls.insert(j, i)
                    break
        for i in n_ls:
            i.show()
manager = URLManager()
manager.add_url("千锋","www.1000phone.net",5)
manager.add_url("百度","www.baidu.com",4)
manager.add_url("腾讯","www.qq.com",1)
manager.add_url("淘宝","www.taobao.com",2)
manager.add_url("python","www.python.org/.net",3)
manager.sorting_stars()







