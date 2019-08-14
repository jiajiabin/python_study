import pymysql
import random

# 链接mysql服务器
db = pymysql.connect("192.168.53.126", "jiabin", "123456", "database_py")

# 创建db游标
cursor = db.cursor()

#执行SQL
sql = """INSERT INTO students
    (id, name, age)
    VALUES
    (%d, '%s', %d);
    """

names = ["one", "two", "three", "four", "five",
         "six", "seven", "eight", "nine", "ten"]
try:
    for i in range(len(names)):
        cursor.execute(sql % (i, names[i], random.randint(13, 18)))
except pymysql.err.IntegrityError as e:
    print(e)
db.commit()
db.close()