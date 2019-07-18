'''
输入起始值，结束值和步数（step）数数
如输入：1 9 2
输出 1 3 5 7 9
'''
a = int(input("起始值"))
b = int(input("结束值"))
s = int(input("步数"))
ss = 0
for i in range(a ,b+1 ,s):
    ss += 1
print(ss)