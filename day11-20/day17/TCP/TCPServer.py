import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.53.6", 6666))

server_socket.listen(3)

while True:
    client_socket, addr = server_socket.accept()
    data = client_socket.recv(1024)
    print(data.decode("utf-8"))
    client_socket.send("你也好".encode("utf-8"))




