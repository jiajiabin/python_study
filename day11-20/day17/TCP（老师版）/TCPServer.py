import socket
# 服务端

# 1.配置套接字 首先设置数据传输方式为TCP，然后绑定IP和端口
# AF_INET 表示我们使用的IP地址是IPv4
# AF_INET6 表示使用的IP地址是IPv6
# SOCK_STREAM 表示使用的是TCP协议
# SOCK_DGRAM 表示使用UDP协议
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.53.133", 8923))
# 服务器上有很多的程序，很多的进程。通过端口找到指定的进程

# 2.监听客户端的链接请求，参数是最大并发数
server_socket.listen(3)
# 如果没有任何链接，程序就一直卡在这里

# 如果有人发起请求，则向下执行
while True:
    # 3.建立链接，返回客户端的IP和端口
    client_socket, addr = server_socket.accept()
    # 接收客户端发来的数据了
    data = client_socket.recv(1024)
    # 不能超过4096，一般是2的幂数，如果不是2的幂数，可能出现中文乱码
    print(data.decode("utf-8"))
    # 发来的数据是二进制，需要解码后使用
    client_socket.send("你也好腻害!!".encode("utf-8"))
