#! /usr/bin/python


from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Random import get_random_bytes

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

def generatePublicKey():
    secret_code = "Unguessable"
    key = RSA.generate(2048)
    encrypted_key = key.exportKey(passphrase=secret_code, pkcs=1,
                                    protection="scryptAndAES128-CBC")
    file_out = open("/carpetaDocker/rsa_key.pem", "wb")
    file_out.write(encrypted_key)


def readPublicKey():
    secret_code = "Unguessable"
    encoded_key = open("/carpetaDocker/rsa_key.pem", "rb").read()
    key = RSA.import_key(encoded_key, passphrase=secret_code)
    print ("Public: ", key.publickey().exportKey())

def encryptar():
    RSAKey = RSA.generate(1024)
    print("hoja")
    publickey = RSAKey.publickey() # pub key export for exchange
    print("inclusion")
    cipher_rsa = PKCS1_OAEP.new(publickey)
    encrypted = cipher_rsa.encrypt("hola".encode('utf-8'))
    #message to encrypt is in the above line 'encrypt this message'

    print ('encrypted message: ', encrypted) #ciphertext
    cipher_rsa = PKCS1_OAEP.decrypt(encrypted)
    decrypted = cipher_rsa
    print ('\ndecrypted', decrypted)


def encryptar2():
    publickey = RSA.generate(1024)
    cipher_rsa = PKCS1_OAEP.new(publickey)
    encrypted = cipher_rsa.encrypt("hola".encode('utf-8'))
    print ('encrypted message: ', encrypted)
    decrypted = cipher_rsa.decrypt(encrypted)
    print ('\ndecrypted', decrypted)

generatePublicKey()
readPublicKey()
encryptar2()

	
#print trustedHost("365.254.21.4")
#concatMessage("Uno Dos Tres Cuatro Cinco fin")
#createServer_Client(int(os.environ.get('portServer')), "localhost")



# docker build -t face .
# docker run -v /home/wagcm/Escritorio/Tarea2_SO/carpetaDocker:/carpetaDocker face
