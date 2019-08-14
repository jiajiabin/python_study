import pymysql
import random

db = pymysql.connect("192.168.53.126", "jiabin", "123456", "homework")
cursor = db.cursor()

sql = """INSERT INTO students
    (id, name, score, class)
    VALUES
    (%d, '%s', %d, %d);
    """
name = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
        'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 
        'u','v', 'w', 'x', 'y', 'z']
for i in range(26):
    cursor.execute(sql % (i, name[i], random.randint(0, 100), random.randint(1901, 1905)))

db.commit()
db.close()