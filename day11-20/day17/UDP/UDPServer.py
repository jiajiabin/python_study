import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("192.168.53.6", 6666))

while 1:
    data, addr = server_socket.recvfrom(1024)
    data = data.decode("utf-8")
    print(data)
    server_socket.sendto("已收到【{}】".format(data).encode("utf-8"),addr)