import socket
host_nuevo = input("Escribe el host: ")
HOST = host_nuevo
PORT = 6030
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))
while 1:
	data = input("Escrbe el mensaje: ")
	print("Esta escribiendo un mensaje…\n")
	socket.send(data.encode("utf-8"))
	mensaje = socket.recv(1024)
	print (mensaje)

socket.close()

