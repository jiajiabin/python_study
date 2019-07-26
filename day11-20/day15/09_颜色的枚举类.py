from enum import Enum
# 枚举类未必只是返回有限数量的数据
# 例如一个颜色的枚举类

class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    @classmethod
    def color(cls, r, g, b):
        return (r, g, b)

color = Color.RED
print(color.value)
color = Color.color(45, 67, 88)
print(color)
