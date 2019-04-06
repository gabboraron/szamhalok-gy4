import socket
import struct
import select

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 22223)
sock.bind(server_address)

inputs = [sock]
sock.listen(1)
while True:
	ready_to_read_from, ready_to_write_on,some_exception = select.select(inputs,[],[])
	for s in ready_to_read_from:
		if s is sock:
			connection, client_address = s.accept()
			inputs.append(connection)
			print('Kapcsolodott valaki')
		else:
			data = s.recv(1024)
			if data:
				unpacker = struct.Struct('I 1s I')
				unpacked_data = unpacker.unpack(data)
				reply = eval(str(unpacked_data[0]) + str(unpacked_data[1]) + str(unpacked_data[2]))
				s.sendall(str(reply))
			else:
				s.close()
				inputs.remove(s)

