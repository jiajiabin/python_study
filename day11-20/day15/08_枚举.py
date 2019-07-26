from enum import Enum

# 继承官方的枚举类Enum即可获得一个枚举类
class Day(Enum):
    # 设置枚举值 枚举值要求全字母大写，单词之间用下划线隔开。
    MONDAY = "星期一"
    TUESDAY = "星期二"
    WEDNESDAY = "星期三"
    THURSDAY = "星期四"
    FRIDAY = "星期五"
    SATURDAY = "星期六"
    SUNDAY = "星期日"
    # 等号前面的是枚举值，等号后面的，是枚举值的值
    # 枚举值不可重复，枚举值的值是不可变数据


d = Day.SUNDAY
print(d.value)

x: Day = Day.FRIDAY
print(x.value)
print(Day.SATURDAY.value)

if x == Day.FRIDAY:
    print("相等")

