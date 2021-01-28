import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.bind((HOST, PORT))
connection.listen(1)

conn, addr = connection.accept()
print('Connected by', addr)
while 1:
    data = conn.recv(1024)
    print(data)
    if not data: break
    conn.sendall(data)
conn.close()
