import pymysql

# 链接mysql服务器
db = pymysql.connect("192.168.53.126", "jiabin", "123456", "database_py")

# 创建db游标
cursor = db.cursor()

# 查询的sql语句
sql = """
        SELECT name, age FROM students WHERE age > 14;
    """

cursor.execute(sql)
# 获取执行的结果
ret = cursor.fetchall()
for i in ret:
    print(i)
    # print("id:%d, name:%s, age:%d" % (i[0], i[1], i[2]))

db.close()