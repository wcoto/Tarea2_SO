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
    print("\n\nServidor esperando clientes...")

    while True:
        conn, addr = server.accept()
        if(trustedHost(addr[0]) == True):
            print ("Conectado con: " + addr[0] + ":" + str(addr[1]))
            data = conn.recv(1024)
            print ("Cliente dice: ", data)
            key = generateKey()
            #message = decryptar(key, data)
            message = concatMessage(data.decode("utf-8"))
            print ("Mensaje: ", message)
            data = encryptar(key, message)
            print ("Encriptado: ", data)
            #if (message != "fin"):
                #data = encryptar(key, message)
                #client = socket.socket()
                #client.connect((ipClient, portClient))
                #client.send("Encriptado_Enviar")
                #client.close()
            conn.close()
        else:
            conn.send("Su conexion no es permitida en este sistema".encode())
            conn.close()
    server.close()

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
        return "fin"
    else:
        new = open("/carpetaDocker/mensaje.txt", "r+")
        message = message + " " + new.readline() + " "
        new.close()
        return message

def generateKey():
    publicKey = RSA.generate(1024)
    cipher_rsa = PKCS1_OAEP.new(publicKey)
    return cipher_rsa

def decryptar(key, encrypted):
    return key.decrypt(encrypted)

def encryptar(key, message):
    return key.encrypt(message.encode('utf-8'))

#def encryptar(message):
    #publickey = RSA.generate(1024)
    #print ("Public: ", publickey.exportKey())
    #cipher_rsa = PKCS1_OAEP.new(publickey)
    #encrypted = cipher_rsa.encrypt(message.encode('utf-8'))
    #print ('\nEncrypted message: ', encrypted)
    #decrypted = cipher_rsa.decrypt(encrypted)
    #print ('\nDecrypted message', decrypted)

def myIP():
    desktop_Name = socket.gethostname()
    direction_IP = socket.gethostbyname(desktop_Name)
    return direction_IP

server()

#myIP()
	
#print trustedHost("365.254.21.4")
#concatMessage("Uno Dos Tres Cuatro Cinco fin")


# docker build -t face .
# docker run -p 15951:15951 -v /home/wagcm/Escritorio/Tarea2_SO/carpetaDocker:/carpetaDocker face


#b'\x07\xfb\xf8\xf3\x13|w\xbb\xf9n\xda\xba\xb6\x81\xea\x15\t\x86M\x16W\xac\xb8\x9dL@\x12\xf2\xbd*h%c \xd7!\x04y\x1d\x99\xf1\t\x13b\x17`}&\xfa\rx\xd7aLf9\xa6K\xffx\x91\x16d\xc1\xcd\xba\x82c\xa2\xe9\xf1m\xbf\\_\x1e\xe4s\x8c\xd4\x1cW\x8d\x02\x0cX\x00\xe9\x94\xd5\xa7\x88\x8f\x85\x8c\xea\x82\xe6W\x03\x8c*\xf8\x7fi/\xd7)H\xae\x92\xe7\xbb\xad\x0b8\xde\xb7\xb5D\x06m\xd6\x98Y\x97\xe2\xb4'