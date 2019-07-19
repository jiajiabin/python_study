import datetime
import time

# 闭包函数往往通过返回值，返回一些附加的功能
def print_num():
    for i in range(1, 101):
        time.sleep(0.1) # 线程休眠，程序等待0.1秒，什么都不做
        print(i)


# 计算这个函数执行需要多久的耗时
# 写一个闭包函数完成这个功能
def count_time():
    def do_count_time(f):           # f = print_num
        # 获取函数f执行之前的时间
        time = datetime.datetime.now()
        f()         # 执行print_num
        # 获取执行完毕的时间
        time2 = datetime.datetime.now()
        return (time2 - time).total_seconds()
    return do_count_time

# 外面这个函数，就是【装饰器】的名字。
# x = count_time()
# print(x(print_num))
t = count_time()(print_num)
print(t)


# def do_count_time(f):  # f = print_num
#     # 获取函数f执行之前的时间
#     time = datetime.datetime.now()
#     f()
#     # 获取执行完毕的时间
#     time2 = datetime.datetime.now()
#     return (time2 - time).total_seconds()
#
#
# t = do_count_time(print_num)
