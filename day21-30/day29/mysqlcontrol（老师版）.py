import pymysql

# 封装一个类，其对象，管理一个数据库
class MySQLControl:
    """
    ================实现基础的链接和关闭===================
    """
    def __init__(self, host, username, password, database):
        self.__host, self.__username, self.__password, self.__database\
        = host, username, password, database
        self.__db = self.__cursor = None

    # 当对象被销毁前，即没有任何引用再使用该对象，调用下面方法
    def __del__(self):
        self.__db.close()

    # 链接mysql服务器
    def connect(self):
        if self.__db:
            self.__db.close()
        self.__db = pymysql.connect(self.__host, self.__username, self.__password, self.__database)
        self.__cursor = self.__db.cursor()

    """
    ================同一个对象允许修改部分参数，重新链接===================
    """
    @property
    def host(self):
        return self.__host
    @host.setter
    def host(self, value):
        self.__host = value

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def database(self):
        return self.__database
    @database.setter
    def database(self, value):
        self.__database = value


    """
    ================创建/删除一个表===================
    """
    # colum_dict == { "id": "INT", "name": "VARCHAR(10)"} contact_dict: dict == { "id": "NOT NULL"}
    def create_table(self, table_name: str, column_dict: dict, contact_dict: dict = None, primary_key: list = None, encoding="utf8"):
        # 写入sql语句
        sql = """
            CREATE TABLE IF NOT EXISTS %s
            (
            %s
            )DEFAULT CHARSET = %s;
        """
        # 完善column列表
        column_content = ""
        if not contact_dict:
            contact_dict = {}
        for i in column_dict:
            if i not in contact_dict.keys():
                contact_dict[i] = ""
            # 创建一个列
            col = "%s %s %s," % (i, column_dict[i], contact_dict[i])
            column_content += col
        column_content = column_content[:-1]
        if primary_key:
            column_content += ", PRIMARY KEY(%s)" % (",".join(primary_key))

        # 完成SQl语句并执行
        sql = sql % (table_name, column_content, encoding)
        self.__cursor.execute(sql)

    def delete_tables(self, table_names: list):
        sql = "DROP TABLE %s" % ",".join(table_names)
        self.__cursor.execute(sql)


    """
    ================数据的修改===================
    """

    # 同步提交
    def commit(self):
        self.__db.commit()

    # 插入数据
    def insert_data(self, table_name, column_value_dict: dict, commit=False):
        sql = """
            INSERT INTO %s
            (%s)
            VALUES
            (%s);
        """
        s1 = ",".join(column_value_dict.keys())

        ls = []
        for i in column_value_dict.values():
            if isinstance(i, str):
                ls.append("'%s'" % i)
            else:
                ls.append(str(i))

        s2 = ",".join(ls)

        self.__cursor.execute(sql % (table_name, s1, s2))
        if commit:
            self.__db.commit()


    # 删除记录
    def delete_record(self, table_name, where: list = None, order_by:dict = None, limit = None,
                      relation_AND=True, commit=False):
        sql = """
            DELETE FROM %s
        """
        if where:
            sql += self.__join_where_tuples(where, relation_AND)
        if order_by:
            sql += self.__join_order(order_by)
        if limit:
            sql += self.__join_limit(limit)

        self.__cursor.execute(sql % table_name)
        if commit:
            self.__db.commit()

    # 修改一个记录
    def update_record(self, table_name, content_set: dict, where: list = None, order_by:dict = None, limit=None,
                      relation_AND=True, commit=False):
        sql = """
            UPDATE %s
            SET %s
        """
        s = ""
        for k in content_set:
            v = content_set[k]
            if isinstance(v, str):
                v = "'%s'" % v
            else:
                v = str(v)
            s += " %s = %s," % (k, v)
        sql = sql % (table_name, s[:-1])

        if where:
            sql += self.__join_where_tuples(where, relation_AND)
        if order_by:
            sql += self.__join_order(order_by)
        if limit:
            sql += self.__join_limit(limit)

        self.__cursor.execute(sql)
        if commit:
            self.__db.commit()

    # 筛选记录
    def select_records(self, table_name, column_list: list = None, where: list = None, order_by:dict = None, limit=None,
                      relation_AND=True):
        sql = """
        SELECT %s FROM %s 
        """
        if column_list:
            sql = sql % (",".join(column_list), table_name)
        else:
            sql = sql % ("*", table_name)

        if where:
            sql += self.__join_where_tuples(where, relation_AND)
        if order_by:
            sql += self.__join_order(order_by)
        if limit:
            sql += self.__join_limit(limit)

        self.__cursor.execute(sql)
        return self.__cursor.fetchall()





    """
    ================条件语句辅助函数===================
    """

    # 拼接where
    def __join_where_tuples(self, where: list, relation_AND):
        # where == (("name", "%张三%", "like"), ("age", 15))
        where_list = []
        for i in where:
            if len(i) >= 3 and i[2].lower() == "like":
                sign = "LIKE"
            elif len(i) >= 3 and i[2] in "> < >= <= !=":
                sign = i[2]
            else:
                sign = "="
            if isinstance(i[1], str):
                s = "%s %s '%s'" % (i[0], sign, i[1])
            else:
                s = "%s %s %s" % (i[0], sign, i[1])
            where_list.append(s)
         # and和or
        if relation_AND:
            relation = "AND"
        else:
            relation = "OR"
        return (" WHERE %s " % (" %s " % relation).join(where_list)).replace("%", "%%", 10000)


    # 拼接order
    def __join_order(self, order:dict):
        # {"score": True, "name":False}
        # "score , name AS DESC"
        ls = []
        d = {True: "", False: "DESC"}
        for key in order:
            ls.append(" %s %s " % (key, d[order[key]]))

        return " ORDER BY %s " % (",".join(ls))

    # 拼接limit
    def __join_limit(self, limit):
        return " LIMIT {}".format(limit)






