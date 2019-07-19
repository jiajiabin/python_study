
class Trapezoid:
    top, bottom, height = 0.0, 0.0, 0.0

    def get_area(self):
        return (self.top + self.bottom) * self.height / 2

    def set_top_bottom_height(self, top, bottom, height):
        self.top, self.bottom, self.height = top, bottom, height


t1 = Trapezoid()
t1.top = 6
t1.bottom = 8
t1.height = 4

print(t1.get_area())

t1.set_top_bottom_height(4, 7, 3)

print(t1.get_area())

