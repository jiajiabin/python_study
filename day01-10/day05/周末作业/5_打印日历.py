"""
周末作业:
日历是以1900年1月1日00：00：00 为基础的 那天的星期1是已知的
时间戳 --- 将已知时间获取其对应的秒数  --- 是以1970年1月1号为基础
2017年10月1日
星期日  	一  	二  	三  	四  	五  	六
    1       2		3       4		5		6		7
    2       9		10		11		12		13		14
    15		16		17		18		19		20		21
换行的时候的规则:
(空格数 + 日期号) % 7 == 0
0 0 0 0 1 2 3
4 5 6 7 8 9 10
"""


def judge_month(year=1900, month=1):
    leap_year = 0
    month_days = 0
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        leap_year = 1
    else:
        leap_year = 0
    if month == 2:
        if leap_year == 1:
            month_days = 29
        else:
            month_days = 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        month_days = 31
    else:
        month_days = 30
    return month_days


def calendar(year=1900, month=1):
    days = 0
    if year < 1900:
        return "输入年份小于1900，没有万年历"
    else:
        days = year * 365 + ((year-1) // 4) - ((year-1) // 100) + ((year-1) // 400)
        days -= 693960
    for i in range(1, month):
        days += judge_month(year, i)
    week = days % 7
    print_calendar(week, year, month)


def print_calendar(week=0, year=1900, month=1):
    print("%.4d年%.2d月的日历" % (year, month))
    print("星期日\t星期一\t星期二\t星期三\t星期四\t星期五\t星期六")
    week += 1
    # for i in range(1,judge_month(year, month)+1):
    n = 0
    num = 0
    print(" ", end="")
    while 0 < week < 7:
        week -= 1
        n += 1
        print(" ",end="")
        print("\t\t", end="")
    while num < judge_month(year, month):
        n += 1
        num += 1
        print(" ","%.2d"%(num),end="")
        print("\t", end="")
        if n == 7:
            print("\n")
            n = 0


calendar(year=int(input("输入年份：")), month=int(input("输入月份：")))











