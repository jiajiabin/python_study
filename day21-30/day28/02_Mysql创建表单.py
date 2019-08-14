import pymysql

# 链接mysql服务器
db = pymysql.connect("192.168.53.126", "jiabin", "123456", "database_py")

# 创建db游标
cursor = db.cursor()

# 通过游标可以执行sql语句
sql = """CREATE TABLE IF NOT EXISTS students
        (id INT PRIMARY KEY,
        name VARCHAR(30) NOT NULL,
        age INT DEFAULT 15
        );
        """

# 执行sql语句
cursor.execute(sql)

db.close()