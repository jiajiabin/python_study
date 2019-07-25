class Anything:
    def git_thing(self,thing):
        print(thing)

class Fabaoji:
    def __init__(self):
        self.str1 = "000"
    def fabao(self,anything:Anything):
        anything.git_thing(self.str1)
        print("发送完成")

fa1 = Fabaoji()
a1 = Anything()
fa1.fabao(a1)
