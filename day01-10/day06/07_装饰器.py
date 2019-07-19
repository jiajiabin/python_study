import datetime
import time

def count_time(function):      # *a **b表示可以传入任何参数       function = print_anything
    def do_count_time(*a, **b):
        # 提前引入，作用是闭包的函数引用外部函数的变量
        nonlocal function       # function = print_anything
        # 获取函数f执行之前的时间
        time = datetime.datetime.now()
        ret = function(*a, **b)      # 表示将任何参数原封不动传入function
        # 获取执行完毕的时间
        time2 = datetime.datetime.now()
        print("执行时间",(time2 - time).total_seconds())
        return ret
    return do_count_time


@count_time     # 装饰当前函数
def print_anything(s: str, times:int):
    for i in range(times):
        print(s)
        time.sleep(0.1)

print_anything("123", 4)
# count_time(print_anything)("123", 4)


