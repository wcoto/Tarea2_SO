import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 9992))

while True:
      mensaje = raw_input("> ")
      s.send(mensaje)
      if mensaje == "quit":
         break

print "adios"

s.close()
