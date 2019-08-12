class Saint:
    def __init__(self, name):
        self.__name = name

    def dead(self):
        print("{}倒下了".format(self.__name))

    def getin(self):
        print("{}登场".format(self.__name))

class Xingshi(Saint):
    def __init__(self):
        super().__init__("星矢")

    def tianmaliuxingquan(self):
        print("星矢击出[天马流星拳]")

    def tianmahuixingquan(self):
        print("星矢击出[天马彗星拳]")

class Zilong(Saint):
    def __init__(self):
        super().__init__("紫龙")

    def lushanshenglongba(self):
        print("紫龙击出[庐山升龙霸]")

    def lushanlongfeixiang(self):
        print("紫龙击出[庐山龙飞翔]")

class Binghe(Saint):
    def __init__(self):
        super().__init__("冰河")

    def zuanshixingchenquan(self):
        print("冰河击出[钻石星尘拳]")

    def shuguangnvshenzhikuanshu(self):
        print("冰河击出[曙光女神之宽恕]")
