# 字符串是一由一串字符组成的数据结构
s = "0123456789"

# 字符串的打印
print(s)
# 字符串的格式化打印
# 格式化打印，可以将其他类型的数据内嵌到字符串中，统一输出
# y, m, d = int(input()), int(input()), int(input())
# 方式1
# s = "{}年{}月{}日".format(y, m, d)
# print(s)

s = "姓名:{}，年龄:{}，身高:{}，体重:{}".format("张三", 15, 1.58, 69)
print(s)

s = "姓名:{0}, 年龄:{1}, 姓名:{0}".format("张三", 15)
print(s)

# 方式2
s = "姓名:%s, 年龄:%d, 身高:%f，体重:%f" % ("李四", 18, 1.78, 78)
# %s 对应字符串， %d对应整型 %f对应浮点
print(s)

# 进制转换
a = 37
print("%d" % a)     # 十进制整型
print("%o" % a)     # 八进制整型
print("%x" % a)     # 十六进制整型

# 保留小数位数
print("%f" % 1.579)
print("%.2f" % 1.579)
print("%.10f" % 1.579)

# 整型对齐
h, m, s = 14, 7, 35
print("%d:%d:%d" % (h, m, s))
print("%2d:%2d:%2d" % (h, m, s))
print("%-2d:%-2d:%-2d" % (h, m, s))
print("%.2d:%.2d:%.2d" % (h, m, s))


# 修改print函数最后字符
# print这个函数会自动在打印结束的时候，添加一个“\n”
for i in range(1, 10):
    for j in range(1, i + 1):
        print("{}X{}={}".format(j, i, i * j), end="\t\t")
    print()




