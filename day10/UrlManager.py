# URLItem，用于存储一个书签的信息
class URLItem:
    def __init__(self, title, url, stars):
        self.__title, self.__url, self.__stars, self.__visits = title, url, stars, 0
        # 成员变量，声明为__开头，则该变量只能通过self，在当前类的成员方法中调用，不能在类外调用

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

    # 打印一个书签的信息
    def show(self):
        print("".center(30, "="))
        print("标题:{}\n网址:{}\n星级:{}\n访问次数:{}".format(self.__title, self.__url, "*" * self.__stars, self.__visits))
        print("".center(30, "="))


# URLManager 储存并管理大量的书签
class URLManager:
    def __init__(self):
        self.__list = []        # 创建一个收藏夹的同时创建list

    # 在列表中查找这个标题的书签
    def __find_urlitem(self, title):
        for i in self.__list:
            if i.get_title() == title:
                return i
        return None

    # 添加书签
    def add_url(self, title: str, url: str, stars: int):
        # 先去找，列表里有没有这个书签
        item = self.__find_urlitem(title)
        if item:                                    # 返回一个对象，所有对象都是真，只有None是假
            print("标题为【{}】的书签已存在，添加失败".format(title))
            return

        item = URLItem(title, url, stars)           # 创建书签
        self.__list.append(item)                    # 添加到列表
        print("书签【{}】已添加成功".format(title))

    # 删除书签(通过标题，通过网址)
    def remove_url(self, title):
        # 寻找需要删除的书签
        item = self.__find_urlitem(title)
        if not item:
            print("书签【{}】不存在，删除失败".format(title))
            return

        # 如果存在，item就是
        self.__list.remove(item)
        print("书签【{}】已删除成功".format(title))


    # 修改书签的标题（通过旧标题，查找书签）
    # 修改书签的网址
    # 修改书签的星级
    # 将所有书签按照访问次数排序后输出
    # 将所有书签按照星级排序后输出


manager = URLManager()
manager.add_url("千锋", "www.1000phone.net", 5)
manager.add_url("百度", "www.baidu.com", 4)
manager.add_url("百度", "www.baidu.com", 4)
manager.remove_url("百度")
manager.add_url("百度", "www.baidu.com", 4)


