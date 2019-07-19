'''
输入时分秒，打印这个时间往后，1小时的所有秒数
如输入：23：12：13
输出：23：12：14
	23：12：15
	...
'''
# h = int(input("时："))
# m = int(input("分："))
# s = int(input("秒："))

sj = str(input("时间："))
h = int(sj[0]) * 10 + int(sj[1])
m = int(sj[3]) * 10 + int(sj[4])
s = int(sj[6]) * 10 + int(sj[7])
for i in range(1, 3601):
    s += 1
    if s == 60:
        m += 1
        s = 0
        if m == 60:
            h += 1
            m =0
            if h == 24:
                h = 0
    print("%.2d:%.2d:%.2d"%(h, m, s))


