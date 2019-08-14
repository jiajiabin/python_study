import pymysql

# 链接数据
db = pymysql.connect("192.168.53.126", "jiabin", "123456", "student_db")

# 创建一个数据库游标（指针，和鼠标指针是一个单词）
cursor = db.cursor()

# 检测链接
cursor.execute("SELECT VERSION()")

# 获取结果
data = cursor.fetchone()

print(data)

db.close()








