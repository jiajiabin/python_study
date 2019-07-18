# .设计一个账户信息的类
# 包含属性：
# 用户名
# 密码
# 昵称
# 注册时间：
# 最后访问时间：
# 包含方法：
# 访问（修改最后访问时间）
# 修改密码(要求传入旧密码和新密码，旧密码正确才能修改)
# 打印账户信息

import datetime

class account:
    def __init__(self):
        self.name : str
        self.password : int
        self.nickname :str
        self.start_time = datetime.datetime.now()
        self.end_time = self.start_time
    def set_name(self,name):
        self.name = name
    def set_password(self,password):
        self.password = password
    def set_nickname(self,nickname):
        self.nickname = nickname
    def visit(self):
        self.end_time = datetime.datetime.now()
    def amend_password(self,new_password):
        self.password = new_password
    def print_message(self):
        print('用户名:%s,昵称：%d,注册时间：%d,最后访问时间：%d'%(self.name,self.nickname,self.start_time,self.end_time))
