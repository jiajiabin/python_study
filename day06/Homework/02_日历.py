
while True:
    y = int(input("请输入一个年份:"))
    m = int(input("请输入一个月份:"))
    if m < 1 or m > 12:
        print("输入错误，请重试!")
    else:
        break

# 编写是否是闰年的判断函数
def is_leap(year):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    else:
        return False


ret = is_leap(y)
if ret:
    print("是闰年")
else:
    print("不是闰年")


# 编写判断当月几天的函数
def days_of_moth(year, month):
    # 函数里面不能直接使用函数外面声明的变量，如果需要使用，需要传参
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        # 二月
        if is_leap(year):
            return 29
        else:
            return 28

print("当月天数", days_of_moth(y, m))


# 计算，当年1月1日距离1900年1月1日一共多少天
def days_sub(year):
    if 1900 > year:
        _max = 1900
        _min = year
    else:
        _max = year
        _min = 1900
    s = 0
    for i in range(_min, _max):
        if is_leap(i):
            s += 366
        else:
            s += 365
    return s

# 计算当月1号，距离当年1月1日多少天
def days_sub_month(year, month):
    s = 0
    for i in range(1, month):           # 若当前月份是五月，只需累加一到四月的天数
        s += days_of_moth(year, i)
    return s

# 求总天数
f = days_sub(y) + days_sub_month(y, m)

#计算星期几
def day_number(f):
    ls = ["星期二", "星期三", "星期四", "星期五", "星期六", "星期日", "星期一"]
    return ls[f % 7]

print(day_number(f))


# 打印日历
def print_datetime(year, month):
    print("星期日\t星期一\t星期二\t星期三\t星期四\t星期五\t星期六")
    f = days_sub(y) + days_sub_month(y, m)
    x = f % 7   # x == 0是星期二，加2个空白，x == 4 是星期六加6个空白，x是5是星期日，加0个空白, x是6是星期一，加1个空白
    # x是元素的下表，元素的值是空白的数量
    ls = [2, 3, 4, 5, 6, 0, 1]
    s, count = "", 0
    for i in range(ls[x]):
        s += "\t\t"
        count += 1

    for i in range(1, days_of_moth(year, month) + 1):
        s += str(i) + "\t\t"
        count += 1
        if count % 7 == 0:
            s += "\n"

    print(s)



print_datetime(y, m)
