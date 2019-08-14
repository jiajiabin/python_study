import pymysql

db = pymysql.connect("192.168.53.126", "jiabin", "123456", "homework")
cursor = db.cursor()

sql = """
        SELECT * FROM students;
    """

cursor.execute(sql)
ret = cursor.fetchall()

# 处理接收内容
list1 = []
for i in ret:
    if i[3] not in list1:
        list1.append(i[3])

sql = """CREATE TABLE IF NOT EXISTS a%s
    (id INT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    score INT DEFAULT 0
    );
    """
for i in list1:
    cursor.execute(sql % str(i))

# 数据分类
sql = """INSERT INTO a%s
    (id, name, score)
    VALUES
    (%d, '%s', %d);
    """
for i in ret:
    cursor.execute(sql % (i[3], i[0], i[1], i[2]))
    db.commit()
db.close()