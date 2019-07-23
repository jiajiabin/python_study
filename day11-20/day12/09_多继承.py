class Father:
    a, b, = 0, 0

    @staticmethod
    def dad_say():
        print("打你！！")


class Mother:
    c, d = 0, 0

    @staticmethod
    def mom_say():
        print("揍你！！")


class Child(Father, Mother):
    @staticmethod
    def mom_say():
        print("别打！！")


c = Child()
c.a, c.b, c.c, c.d = 1, 2, 3, 4
c.mom_say()
c.dad_say()


