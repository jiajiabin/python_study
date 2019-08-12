import socket
from user_manager import UserManager

# 服务器的ip和端口
server_addr = ("192.168.53.17", 8080)

# 服务端程序，接收用户请求，做相关处理
class MyChatServer:
    def __init__(self):
        self.__socket = self.init_socket()
        # 用户管理器
        self.__user_manager = UserManager()

    @staticmethod
    # 配置并返回socket
    def init_socket():
        global server_addr
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(server_addr)
        return s

    # 启动函数
    def start(self):
        self.run()

    # 监听客户端发来的请求
    def run(self):
        while True:
            data, addr = self.__socket.recvfrom(1024)
            # 根据客户端发来的数据不同，做不同的处理
            # 解析data
            self.respond_request(data.decode("utf-8"), addr)

    # 根据客户端发来的字符串，了解客户端需求，分发处理
    def respond_request(self, data, addr):
        ctl = data.split("|")[0]
        ctl_dict = {
            # 登陆请求  <[LOGIN]>|username
            '<[LOGIN]>': MyChatServer.client_login,
            # 下线请求 <[LOGOUT]>|username
            '<[LOGOUT]>': MyChatServer.client_logout,
            # 显示在线用户列表 <[SHOW_USR_LIST]>|username
            '<[SHOW_USR_LIST]>': MyChatServer.client_request_user_list,
            # 聊天<[SEND_MESSAGE]>|fromusername|tousername|words
            '<[SEND_MESSAGE]>': MyChatServer.clinet_send_message
        }
        try:
            ctl_dict[ctl](self, data, addr)
        except KeyError:
            print("KeyError")

    # 客户端登陆处理
    def client_login(self, data, addr):
        # 登陆请求  <[LOGIN]>|username
        username = data[10:]
        ret = self.__user_manager.login_user(username, addr)
        if ret:
            # 登陆成功
            print("【{}】登陆成功".format(username))
            # 发一个回执
            content = "<[LOGIN_SUCCESS]>"
            self.__socket.sendto(content.encode("utf-8"), addr)
        else:
            # 登陆失败
            print("【{}】登陆失败".format(username))
            # 发一个回执
            content = "<[LOGIN_FAILED]>"
            self.__socket.sendto(content.encode("utf-8"), addr)

    # 客户端下线处理
    def client_logout(self, data, addr):
        # <LOGOUT>}username
        username = data[11:]
        ret = self.__user_manager.logout_user(username)
        if ret:
            print("【{}】已下线".format(username))
            # 发回执
            content = "<[LOGOUT_SUCCESS]>"
            self.__socket.sendto(content.encode("utf-8"), addr)

    # 客户端请求显示在线用户列表
    def client_request_user_list(self, data, addr):
        content = "<[USR_LIST]>|" + self.__user_manager.get_username_list()
        self.__socket.sendto(content.encode("utf-8"), addr)
        print("发送了请求的在线用户列表to【{}】".format(data[17:]))


    # 转发客户端的聊天信息
    def clinet_send_message(self, data, addr):
        # 聊天<[SEND_MESSAGE]>|fromusername|tousername|words
        ls = data.split("|")
        # 通过usermanager找到tousername的addr
        to_addr = self.__user_manager.get_user_addr(ls[2])
        if not to_addr:
            # 发送回执
            content = "<[SEND_MESSAGE_FAILED]>|目标用户不存在"
            self.__socket.sendto(content.encode("utf-8"), addr)
            return
        # 将信息发送给目标用户
        self.__socket.sendto(data.encode("utf-8"), to_addr)
        print("【{}】向【{}】发送了信息({})".format(ls[1], ls[2], ls[-1]))

chat_server = MyChatServer()
chat_server.start()