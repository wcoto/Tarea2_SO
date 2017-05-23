import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 15951))

while True:
    mensaje = raw_input("> ")
    s.send(mensaje)
    if mensaje == "quit":
        break
    data = s.recv(1024)
    print ("Recibido: " + data)
print "adios"

s.close()
