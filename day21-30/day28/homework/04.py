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

sql = """
        SELECT * FROM a%s;
    """
list2 = []
for i in list1:
    cursor.execute(sql % i)
    ret = cursor.fetchall()
    sum = 0
    for j in ret:
        sum += int(j[2])
    list2.append((i, sum / len(ret)))

max = 0
class_max = None
for i in list2:
    if i[1] > max:
        max = i[1]
        class_max = i[0]
print(class_max)

cursor.execute(sql % class_max)
ret1 = cursor.fetchall()
score_max = 0
name = None
for i in ret1:
    if i[2] > score_max:
        score_max = i[2]
        name = i[1]
print(name)