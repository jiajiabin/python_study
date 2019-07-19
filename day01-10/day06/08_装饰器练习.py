# 装饰器练习
# 写一个装饰器，在一个函数执行之前，打印这个函数将要执行，在函数执行之后，打印执行完毕
# 打印函数执行完毕的时间
import datetime

def run_time(function):
    def do_run_time(*c, **v):
        print("函数将要执行")
        nonlocal function
        ret = function(*c, **v)
        print("函数执行完毕，时间", datetime.datetime.now())
        return ret
    return do_run_time


@run_time
def print_helloworld():
    print("hello world!")

print_helloworld()