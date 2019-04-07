import socket
import struct

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 22223)

connection.connect(server_address)

values = (int(input()), str(input()).encode('UTF-8'), int(input()))
packer = struct.Struct('I 1s I')
packed_data = packer.pack(*values)

connection.sendall(packed_data)
data = connection.recv(1024)
print(data.decode('UTF-8'))

connection.close()
