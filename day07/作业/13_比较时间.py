# 编写函数※※传入10个时间，找出最大的一个传入格式[00:00:00]
def compare_time(*args):
    max1 = 0
    for i in args:
        h = i[:-6]
        m = i[-5:-3]
        s = i[-2:]
        sec = int(h) * 3600 + int(m) * 60 + int(s)
        if sec > max1:
            max1 = sec
    h1 = max1 // 3600
    m1 = max1 // 60 % 60
    s1 = max1 % 60
    return "[%d:%d:%d]" % (h1, m1, s1)

print(compare_time('01:12:12','04:34:34'))
