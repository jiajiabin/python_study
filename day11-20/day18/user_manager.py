class User:
    def __init__(self, username, addr):
        self.__username = username
        self.__addr = addr

    @property
    def username(self):
        return self.__username

    @ username.setter
    def username(self, v):
        self.__username = v

    @property
    def addr(self):
        return self.__addr

    @addr.setter
    def addr(self, v):
        self.__addr = v


# 上线用户管理， 上线添加到列表，下线从列表删除
class UserManager:
    def __init__(self):
        self.__user_list = []

    # 查找函数
    def __find_user(self, name):
        for i in self.__user_list:
            if i.username == name:
                return i
        return None

    # 一个用户登陆上线
    def login_user(self, username, addr):
        user = self.__find_user(username)
        if user:
            # 添加失败
            return False
        # 创建并添加
        user = User(username, addr)
        self.__user_list.append(user)
        return True

    # 下线
    def logout_user(self, username):
        user = self.__find_user(username)
        if user:
            self.__user_list.remove(user)
            return True
        return False

    # 返回所有在线用户列表
    def get_username_list(self):
        usernames = [i.username for i in self.__user_list]
        return '|'.join(usernames)

    # 根据用户名返回addr
    def get_user_addr(self, name):
        user = self.__find_user(name)
        if user:
            return user.addr
        return None
