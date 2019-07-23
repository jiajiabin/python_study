class List(list):
    def print_self(self):
        x = 0
        for i in self:
            print("元素%d" % x, i)
            x += 1


l = List()
l.extend([1, 2, 3, 4, 5])
l.print_self()
