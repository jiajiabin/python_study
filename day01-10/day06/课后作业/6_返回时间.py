# 1.编写一个函数参数传入一个秒数，返回时间字符串
# 传入：61
# 返回：00:01:01

def return_time(time_second):
    s = time_second % 60
    m = time_second // 60 % 60
    h = time_second // 3600 % 24
    print("%.2d时%.d分%.2d秒" % (h, m, s))


return_time(int(input("输入一个秒数")))
