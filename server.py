import socket


HOST = ''
PORT = 6030
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(2)
conexion, address = socket.accept()
print ("Cliente: ", address)

while 1:
	data = conexion.recv(1024)
	if not data:
		break
	else:
		print (data)
		#coneccion.send(data)
		dataa = input("Escrbe una respuesta: ")
		conexion.send(dataa.encode("utf-8"))

conexion.close()
