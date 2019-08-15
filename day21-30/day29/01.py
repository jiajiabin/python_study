from mysqlcontrol import MySQLControl
import random

mc = MySQLControl("192.168.53.126", "jiabin", "123456", "student_db")
mc.connect()

mc.delete_tables(["new_table"])
colum_dict = {
    "id":"INT",
    "name":"varchar(30)",
    "score":"float"
}
mc.create_table("new_table", colum_dict, primary_key=["id"])

names = ["熊大", "熊二", "张三", "李四", "王五",
         "赵六", "燕七", "王八", "汾九", "全十",
         "萧十一","月十二","剑十三"]
for i in range(len(names)):
    mc.insert_data("new_table", {"id":i, "name":names[i],"score":random.randint(0,100)})
mc.commit()
#mc.delete_record("new_table", [("name","全十"), ("name","汾九"), ("name","%十%","like")], relation_AND=False, commit=True)
#mc.delete_record(table_name="new_table", where=[("name","%十%","like")], order_by={"id":False}, limit=1, commit=True)
mc.update_record(table_name="new_table",content_set={"name":"王老五"}, where=[("name","王五")], commit=True)

ret = mc.select_records(table_name="new_table", order_by={"score":False},where=[("id","5",">=")])
for i in ret:
    print(i)
