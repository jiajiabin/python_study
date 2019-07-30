import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.53.6", 6666))

client_socket.send("你好".encode("utf-8"))
data = client_socket.recv(1024)
print(data.decode("utf-8"))