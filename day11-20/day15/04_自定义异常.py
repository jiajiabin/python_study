class NegativeError(BaseException):
    def __init__(self, message = "负数错误"):
        super().__init__(message)


class Rect:
    def __init__(self, length, width):
        if length < 0 or width < 0:
            raise NegativeError("矩形的长和宽不能是负数")
        self.__length, self.__width = length, width


try:
    r = Rect(-1, 2)
except NegativeError as e:
    print(e)