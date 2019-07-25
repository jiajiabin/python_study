class ListDelegate:
    def receive_data(self):
        return []

class TraverseList:
    def traverse_list(self,list_source:ListDelegate):
        list2 = []
        list1 = list_source.receive_data()
        for i in list1:
            list2.append(i ** 2)
        return list2