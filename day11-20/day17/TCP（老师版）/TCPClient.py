import socket
# 客户端
# 配置socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 链接服务端IP和端口
client_socket.connect(("192.168.53.133", 8923))

# 链接成功，才会向下执行
client_socket.send("你好毒，你好毒，你好毒毒毒！！".encode("utf-8"))
# 编码为二进制

# 接收回执
data = client_socket.recv(1024)
print(data.decode("utf-8"))

