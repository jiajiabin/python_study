# 如果装饰器修饰的函数带参数呢
import datetime
import time

def print_anything(s: str, times:int):
    for i in range(times):
        print(s)
        time.sleep(0.1)



def count_time(function, *a, **b):      # *a **b表示可以传入任何参数
    def do_count_time():
        # 提前引入，作用是闭包的函数引用外部函数的变量
        nonlocal function, a, b
        # 获取函数f执行之前的时间
        time = datetime.datetime.now()
        ret = function(*a, **b)      # 表示将任何参数原封不动传入function
        # 获取执行完毕的时间
        time2 = datetime.datetime.now()
        print("执行时间",(time2 - time).total_seconds())
        return ret
    return do_count_time

# x = count_time(print_anything, "hello world!", 3)
# t = x()
print_anything("123", 4)
count_time(print_anything, "hello world!", 3)()

def add(a, b, c):
    return a + b + c
s = count_time(add, 1, 2, 3)()
print(s)


