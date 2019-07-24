class Vehicle:
    # 座位数，加速度，刹车距
    def __init__(self, num_of_seats, up_speed, brake_spacing):
        self.__num_of_seats, self.__up_speed, self.__brake_spacing = num_of_seats, up_speed, brake_spacing

    @staticmethod
    def roll_out():
        print("启动")

    @staticmethod
    def stop():
        print("停车")

    @staticmethod
    def speed_up():
        print("加速")

    @staticmethod
    def speed_down():
        print("减速")

    @staticmethod
    def brake():
        print("刹车")


class Truck(Vehicle):
    def __init__(self, num_of_seats, up_speed, brake_spacing, loading_weight):
        super().__init__(num_of_seats, up_speed, brake_spacing)
        self.__loading_weight = loading_weight

    @staticmethod
    def swap():
        print("翻斗")


truck = Truck(2, 60, 100, 5000)
truck.roll_out()
truck.speed_up()
truck.speed_down()
truck.brake()
truck.stop()