ret = input()
# input读取键盘输入的数据赋值给ret，数据类型是str
print("good", int(ret) + 1)
print(type(ret))
# 将ret强制类型转换为int数据，这个转换不会修改ret的类型。是int(ret)这个表达式的值是int类型。
# 就像是 a + 3 == 8 不代表a == 8， a + 3这个表达式的值 == 8

# if 5 < 3:
#     print("Good!")      # python比其他语言更重视缩进
#     print("Good day!")

