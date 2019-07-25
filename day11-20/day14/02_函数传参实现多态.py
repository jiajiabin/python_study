import random


class Stu:
    def __init__(self, name, age, score, height):
        self.__name, self.__age, self.__score, self.__height = name, age, score, height

    @property
    def age(self):
        return self.__age

    @property
    def score(self):
        return self.__score

    @property
    def height(self):
        return self.__height

    def __repr__(self):
        return "【姓名:{}，年龄:{}，成绩:{}, 身高:{}】".format(self.__name, self.__age, self.__score, self.__height)


ls = []
names = ["张三", "李四", "王五", "赵六"]
for name in names:
    ls.append(Stu(name, random.randint(10, 15), random.randint(0, 100), random.randint(135, 180) / 100))
# ls里面有四个学生
print(ls)


# 对学生，根据年龄进行排序, 从小到大排序
# 对学生，根据年龄进行排序, 从大到小排序
def sort(ll, fuction):                   # ll = ls  fuction = older_than
    for i in range(len(ll) - 1):
        for j in range(0, len(ll) - 1 - i):
            if fuction(ll[j], ll[j + 1]):
                ll[j], ls[j + 1] = ll[j + 1], ls[j]


# 写一个比较两个学生的函数，左边的年龄大，返回真
def older_than(stu1, stu2):
    return stu1.age > stu2.age

def younger_than(stu1, stu2):
    return stu1.age < stu2.age

def score_worse(stu1, stu2):
    return stu1.score < stu2.score

def shorter_than(stu1, stu2):
    return stu1.height < stu2.height


sort(ls, older_than)
print(ls)
sort(ls, younger_than)
print(ls)
sort(ls, score_worse)
print(ls)
sort(ls, shorter_than)
print(ls)

