import socket


HOST = '127.0.0.1'
PORT = 1234
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(2)
coneccion, address = socket.accept()
print ("Cliente: ", address)
while 1:
	data = coneccion.recv(1024)
	if not data:
		break
	print (data)
	coneccion.send(data)
coneccion.close()
