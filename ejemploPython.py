#! /usr/bin/python


from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Random import get_random_bytes

import socket
import sys

HOST = ''
PORT = 15951


def server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
    except (socket.error):
        print ("Fallo en el enlace...")
        sys.exit()

    server.listen(10)
    print("Servidor esperando clientes...")

    while 1:
        conn, addr = server.accept()
        print ("Conectado con: " + addr[0] + ":" + str(addr[1]))
        data = conn.recv(1024)
        print(data)
        conn.close

    server.close

# "localhost", 9999
def createServer_Client(portServer, ipServer):
    server = socket.socket()
    #client = socket.socket()

    server.bind((ipServer, portServer))
    server.listen(1)
    sc, addr = server.accept()

    #client.connect((ipClient, portClient))
    while True:
        received = sc.recv(1024)
        if received == "quit":
            break
        print ("Recibido_Encriptado: ", received)
        #client.send("Encriptado_Enviar")

    sc.close()
    server.close()
    #client.close()

def trustedHost(host):
    with open("/carpetaDocker/Configuracion.config", "r+") as reader:
        valor = False
        for line in reader:
            if line.strip("\n") == host:
                valor = True
    reader.close()
    return valor

def isFin(message):
	results = message.split()
	valor = False
	for i in results:
		if (i == "fin"):
			valor = True
	return valor

def concatMessage(message):
	if(isFin(message)):
		end = open("/carpetaDocker/mensaje.txt", "w")
		end.write(message)
		end.close()
	else:
		new = open("/carpetaDocker/mensaje.txt", "r+")
		message = message + " " + new.readline() + " "
		new.close()
		print (message)	

def encryptar(message):
    publickey = RSA.generate(1024)
    print ("Public: ", publickey.exportKey())
    cipher_rsa = PKCS1_OAEP.new(publickey)
    encrypted = cipher_rsa.encrypt(message.encode('utf-8'))
    print ('\nEncrypted message: ', encrypted)
    decrypted = cipher_rsa.decrypt(encrypted)
    print ('\nDecrypted message', decrypted)

server()

	
#print trustedHost("365.254.21.4")
#concatMessage("Uno Dos Tres Cuatro Cinco fin")


# docker build -t face .
# docker run -v /home/wagcm/Escritorio/Tarea2_SO/carpetaDocker:/carpetaDocker face
