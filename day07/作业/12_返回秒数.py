# 编写函数传入一个带中括号的时间，将时间转成秒数
# 传入[00:01:03]你是我的心
# 返回63->你是我的心
def return_second(str1):
    list1 = str1.split("]")
    h = list1[0][1:-6]
    m = list1[0][-5:-3]
    s = list1[0][-2:]
    sec = int(h) * 3600 + int(m) * 60 + int(s)
    return "%d->%s" % (sec, list1[1])


print(return_second("[00:01:03]你是我的心"))
