# 作业：
# 1.设计一个圆的类，通过构造方法初始化半径。包含方法：
# 修改半径：
# 返回周长：
# 返回面积：

class Circle:
    def __init__(self, raidus):
        self.raidus = raidus

    def set_raidus(self, raidus):
        self.raidus = raidus

    def get_area(self):
        return 3.14 * self.raidus ** 2

    def get_perimeter(self):
        return 3.14 * self.raidus * 2

# 2.设计一个分数的类，包含属性：
# 分子
# 分母
# 包含方法：
# 修改分子和分母
# 按照 分子/分母 方式输出
# 约分

class Fraction:
    def __init__(self, s, m):
        self.m, self.s = m, s

    def set_info(self, s, m):
        self.m, self.s = m, s

    def show(self):
        print("{}/{}".format(self.s, self.m))

    def reduce(self):
        # 先求出最大公约数
        sign = 1
        if self.s * self.m < 0:
            sign = -1           # 结果是负数
        self.s = abs(self.s)
        self.m = abs(self.m)    # 全都变成绝对值

        _min = min(self.s, self.m)
        while True:
            if self.s % _min == 0 and self.m % _min == 0:
                break
            else:
                _min -= 1
        self.s //= _min * sign   # 最后将符号给分子
        self.m //= _min


f = Fraction(4, -8)
f.reduce()
f.show()

# 3.设计一个账户信息的类
# 包含属性：
# 用户名
# 密码
# 昵称
# 注册时间：
# 最后访问时间：
# 包含方法：
# 访问（修改最后访问时间）
# 修改密码(要求传入旧密码和新密码，旧密码正确才能修改)
# 打印账户信息
class User:
    def __init__(self, username, password, nickname, register_time, visit_time):
        self.username, self.password, self.nickname, self.register_time, self.visit_time \
            = username, password, nickname, register_time, visit_time

    def set_visit_time(self, new_time):
        self.visit_time = new_time

    def set_passwd(self, old_passwd, new_passwd):
        if old_passwd == self.password:
            self.password = new_passwd

    def show_info(self):
        print("用户名:%s\n昵称:%s\n注册时间:%s\n最后访问时间:%s\n" % (self.username,
                                                       self.nickname, self.register_time, self.visit_time))




# 4.设置矩形类，包含长和宽
# 方法：
# 返回面积
# 返回周长
#
