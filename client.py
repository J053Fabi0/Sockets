import socket

HOST = '127.0.0.1'
PORT = 1234
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))
data = input("Escrbe el mensaje: ")
socket.send(data.encode("utf-8"))
socket.close()

