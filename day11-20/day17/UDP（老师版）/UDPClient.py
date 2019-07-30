import socket

# 配置socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 发送数据
client_socket.sendto("太阳天空照".encode("utf-8"), ("192.168.53.133", 8923))

# 接收回执
data, addr = client_socket.recvfrom(1024)
print(data.decode("utf-8"))
