# 1.输入一个成绩，如果成绩在85-100之间，打印优秀，在60-84之间，打印及格，0-59之间，打印不及格，其他数字打印“输入错误”。
# score = int(input())
# if 85 <= score <= 100:
#     print("优秀")
# elif 60 <= score < 85:
#     print("及格")
# elif 0 <= score < 60:
#     print("不及格")
# else:
#     print("输入错误")

# 2.通过程序，模拟下列分段函数的效果，输入x，输出对应的y值
# y = 	x^2 (x < 0)
# 	    2x + 1 (0 <= x < 5)
# 	    3x - 11 (x >= 5)
x = int(input())
if x < 0:
    y = x ** 2
elif x < 5:
    y = 2 * x + 1
else:
    y = 3 * x - 11

print(y)


