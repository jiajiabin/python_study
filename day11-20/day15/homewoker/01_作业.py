# 1.写一个通用的遍历列表的函数，遍历之后对每个元素干什么（例如打印或者对每个元素求平方），任意。

def travel_do_sth(ls:list, func, *arg):
    for i in ls:
        func(i, *arg)

ls = [1, 2, 3, 4, 5]
travel_do_sth(ls, print, "！！")


# 2. 写一个功能模块，对传入的任何数据，根据任何排序原则，进行排序。然后回调方法，返回排序后的数据。
class SortListDelegate:
    def recieve(self, list): pass

class SortList:
    @staticmethod
    def sort(ls: list, func, reverse: bool, delegate: SortListDelegate):
        ls.sort(key=func, reverse=reverse)
        delegate.recieve(ls)



# 3. 自己写那个字典类，加一个方法，传入英文，将对应的中文，主动的发给任意对象。


