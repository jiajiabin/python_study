class Student:
    # def __init__(self):
    #     self.name = "张三"      # 对象属性
    name = "张三"                 # 类属性
    score_list = []               # 该代码不是在创建对象时调用的，而是在声明类时调用的，程序起始时创建的。只执行一次

s = Student()
s.name = "李四"
s1 = Student()
print(s1.name)

s.score_list.extend([1, 2, 3, 4])
print(s1.score_list)
# s.score_list = [1, 2, 3, 4]
# print(s1.score_list)

Student.name = "王五"     # 类名调用类属性
print(s.name, s1.name)
# 没有单独赋值变量，如s1.name会跟随类一起改变，  单独赋值过的s.name就会保留单独的值。

# class Student:
#     def __init__(self):
#         self.name = "张三"      # 对象属性
#         self.score_list = []
#
# s = Student()
# s.name = "李四"
# s1 = Student()
# print(s1.name)
#
# s.score_list.extend([1, 2, 3, 4])
# print(s1.score_list)