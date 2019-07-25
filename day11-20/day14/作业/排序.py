class ListDelegate:
    def receive_data(self):
        return []
    def sort_way(self):
        return None

class Sort:
    def sort_list(self,list_source:ListDelegate):
        list1 = list_source.receive_data()
        func = list_source.sort_way()
        list1.sort(key=func)
        return list1

class List(ListDelegate):
    def __init__(self):
        self.__list = [1,3,4,6,7,2,9]
    def receive_data(self):
        return self.__list
    def sort_way(self):
        return int
    def show_sort(self):
        show1 = Sort()
        print(show1.sort_list(self))

l1 = List()
l1.show_sort()

