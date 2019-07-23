class car:
    def __init__(self):
        self.__seat_nums = 0
        self.__accelerated_speed = 0
        self.__braking_distance = 0
    def _start(self):
        print("启动")
    def _speed_up(self):
        print("加速")
    def _stop(self):
        print("停车")
    def _speed_cut(self):
        print("减速")
    def _brake(self):
        print("刹车")
class truck(car):
    def __init__(self):
        super().__init__()
        self.__load_capacity = 0
    def load_capacity(self):
        print("翻斗")
class saloon_car(car):
    def __init__(self):
        super().__init__()
        self.__four_wheel = True
class sports_car(saloon_car):
    def __init__(self):
        super().__init__()
        self.__roadster = True
class tricycle(car):
    def __init__(self):
        super().__init__()
        self.__pedal_damping = 0
    def __foot_brake (self):
        print("脚刹")