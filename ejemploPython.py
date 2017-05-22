#! /usr/bin/python

import socket
import os

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
        print "Recibido_Encriptado: ", received
        #client.send("Encriptado_Enviar")

    sc.close()
    server.close()
    #client.close()


def crypt():
	random_generator = Random.new().read
	key = RSA.generate(1024, random_generator) #generate pub and priv key

	publickey = key.publickey() # pub key export for exchange

	encrypted = publickey.encrypt("encrypt this message", 32)
#message to encrypt is in the above line 'encrypt this message'

	print "encrypted message:", encrypted #ciphertext
	f = open ("/carpetaDocker/encryption.txt", "w")
	f.write(str(encrypted)) #write ciphertext to file
	f.close()

#decrypted code below

	f = open("/carpetaDocker/encryption.txt", "r")
	message = f.read()


	decrypted = key.decrypt(ast.literal_eval(str(encrypted)))

	print "decrypted", decrypted

	f = open ("/carpetaDocker/encryption.txt", "w")
	f.write(str(message))
	f.write(str(decrypted))
	f.close()

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
		message = message + " " + new.readline()
		new.close()
		print message	
	
print trustedHost("365.254.21.4")
concatMessage("Uno Dos Tres Cuatro Cinco fin")
#createServer_Client(int(os.environ.get('portServer')), "localhost")
