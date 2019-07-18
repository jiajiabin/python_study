# .设计一个分数的类，包含属性：
# 分子
# 分母
# 包含方法：
# 修改分子和分母
# 按照 分子/分母 方式输出
# 约分
class Score:
    def __init__(self, numerator, denominator):
        self.numerator = int(numerator)
        self.denominator = int(denominator)

    def set_number(self, numerator, denominator):
        self.numerator = int(numerator)
        self.denominator = int(denominator)

    def print_score(self):
        print("%d/%d" % (self.numerator, self.denominator))

    def reduction_fraction(self):
        min1 = min(self.numerator, self.denominator)
        for i in range(min1, 1, -1):
            if self.numerator % i == 0 and self.denominator % i == 0:
                self.numerator /= i
                self.denominator /= i
                return


sc1 = Score(4, 6)
sc1.print_score()
sc1.reduction_fraction()
sc1.print_score()
