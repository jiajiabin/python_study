import pymysql

db = pymysql.connect("192.168.53.126", "jiabin", "123456", "homework")
cursor = db.cursor()

sql = """CREATE TABLE IF NOT EXISTS students
        (id INT PRIMARY KEY,
        name VARCHAR(30) NOT NULL,
        score INT DEFAULT 0,
        class INT DEFAULT 0
        );
        """
cursor.execute(sql)

db.close()