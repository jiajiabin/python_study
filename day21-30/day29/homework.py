import pymysql
import random

# 链接服务器
db = pymysql.connect("192.168.53.145", "ace", "123456", "db_homework")
# 创建游标
cursor = db.cursor()


# 删除表单
sql = """
        DROP TABLE IF EXISTS students, class;
    """
cursor.execute(sql)

# 创建表单
sql = """CREATE TABLE IF NOT EXISTS students
        (
            id VARCHAR(20) PRIMARY KEY,
            name VARCHAR(30) NOT NULL,
            score INT DEFAULT 0,
            class VARCHAR(20)
        )DEFAULT CHARSET = utf8;
        """
# 创建了表单
cursor.execute(sql)

classes_list = ["PY1901", "PY1902", "PY1903", "PY1904"]
names = ["宋江", "卢俊义", "吴用", "公孙胜", "李逵", "柴进", "林冲", "关胜", "呼延灼", "朱仝", "雷横", "燕青", "张清"]

sql = """
        INSERT INTO students
        (id, name, score, class)
        VALUES
        ('%s', '%s', '%d', '%s');
        """

for i in range(len(names)):
    s = sql % ("A%06d" % i, names[i], random.randint(0, 100) ** 0.5 * 10, random.choice(classes_list))
    cursor.execute(s)

db.commit()

# 创建class表单
sql = """CREATE TABLE IF NOT EXISTS class
        (
            class_name VARCHAR(20) PRIMARY KEY,
            number_of_students INT DEFAULT 0,
            avg_score FLOAT
        )DEFAULT CHARSET = utf8;
        """
cursor.execute(sql)

# 填充数据
# 获取班级的名称
sql = """
        SELECT DISTINCT class FROM students ORDER BY class;
    """
cursor.execute(sql)
ret = cursor.fetchall()

# 获取班级人数，和平均分
sql = """
        SELECT score FROM students WHERE class = '%s'
    """

insert_sql = """
        INSERT INTO class
        (class_name, number_of_students, avg_score)
        VALUES
        ('%s', %d, %.2f)
    """
for i in ret:
    cursor.execute(sql % i[0])
    r = cursor.fetchall()       #((45,),(89,),(56,))
    num = len(r)                # 获取成绩数量，即人数
    s = 0
    for j in r:
        s += j[0]
    avg_score = s / num         # 平均成绩
    # 得到了一个班级的人数成绩和班的名称，录入
    cursor.execute(insert_sql % (i[0], num, avg_score))

db.commit()

# 找出班级平均分第一的班级
sql = "SELECT class_name, avg_score FROM class ORDER BY avg_score DESC LIMIT 1"
cursor.execute(sql)
ret = cursor.fetchall()
# 获取年级第一班级名称
class_name = ret[0][0]

# 找出该班学生，成绩排序，取前5名
sql = "SELECT id, name, score FROM students WHERE class = '%s' ORDER BY score DESC LIMIT 5" % class_name
cursor .execute(sql)
ret = cursor.fetchall()
for i in ret:
    print("姓名:%s 学号:%s 成绩:%d" % (i[1], i[0], i[2]))

db.close()


