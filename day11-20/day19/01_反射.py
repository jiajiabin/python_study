# 通过字符串，获取对应方法，并进行调用的机制，称为反射
# 反射的本质就是通过一个字典，根据key查找并调用对应的方法。
# 通过反射，我们可以根据字符串的内容动态的决定调用哪一个方法。创建哪一个对象
# 可以通过网络传输数据或者读取配置文件，改变程序的工作内容。
# 顺便可以实现可视化编程
# Android/iOS 都是通过拖控件的方式创建UI
# 虚幻4引擎 蓝图机制

# 根据字符串调用类中的方法
class Student:
    def show(self):
        print("这是一个学生")

    def study(self):
        print("好好学习，天天向上")


stu = Student()
s = input()

# 第二个参数时字符串，字符串是函数名，第三个参数是如果找不到，返回什么
# 如果成功，则返回函数
# func = getattr(Student, s, None)
# if func:
#     func(stu)

# 获取类创建对象
mo = __import__(s)      # 导入一个包 student
s = input()

func = getattr(mo, s, None)     # 找一个方法 student.Student

obj = func()                    # student.Student()

print(obj)

mo = __import__('__main__')
func = getattr(mo, "Student", None)
obj = func()
print(obj)








