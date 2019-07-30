import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while 1:
    client_socket.sendto("你好".encode("utf-8"),("192.168.53.12", 6404))

    data, addr = client_socket.recvfrom(1024)
    print(data.decode("utf-8"))



