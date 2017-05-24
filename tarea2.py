#! /usr/bin/python


from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Random import get_random_bytes
from base64 import b64decode

import socket
import sys

HOST = ''
PORT = 15951
EXTERN_PORT = 7777
CONFIG = "/carpetaDocker/Configuracion.config"
MESSAGE = "/carpetaDocker/mensaje.txt"
PUBLIC_KEY = "/carpetaDocker/PublicKey.txt"
IP = "/carpetaDocker/ip.txt"
CONDITIONAL = "fin"


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
            print ("\nConectado con: " + addr[0] + ":" + str(addr[1]))
            data = conn.recv(1024)
            message = concatMessage(decryptar(data).decode("utf-8"))
            if (message != "ready"):
                data = encryptar(message.encode('utf-8'))
                clientSend(data)
            conn.close()
        else:
            conn.send("\nSu conexion no es permitida en este sistema\n".encode())
            conn.close()
    server.close()

def clientSend(data):
    indexNextServer = ipIndex() + 1
    ipList = createIPList()
    client = socket.socket()
    client.connect((ipList[indexNextServer], EXTERN_PORT))
    client.send(data)
    client.close()

def ipIndex():
    ipList = createIPList()
    return ipList.index(myIP())

def createIPList():
    ipList = []
    with open(CONFIG, "r+") as reader:
        for line in reader:
            ipList.append(line.strip("\n"))
    reader.close()
    return ipList


def trustedHost(host):
    ipList = createIPList()
    return host in ipList

def isFin(message):
    results = message.split(" ")
    valor = False
    for i in results:
        if (i == CONDITIONAL):
            valor = True
    return valor

def concatMessage(message):
    if(isFin(message)):
        end = open(MESSAGE, "w")
        end.write(message)
        end.close()
        return "ready"
    else:
        new = open(MESSAGE, "r+")
        message = message + " " + new.readline().strip("\n")
        new.close()
        return message

def decryptar(encryptedMessage):
    privateKey = RSA.importKey(open(PUBLIC_KEY, "r+").read())
    cipher = PKCS1_OAEP.new(privateKey)
    return cipher.decrypt(encryptedMessage)

def encryptar(message):
    privateKey = RSA.importKey(open(PUBLIC_KEY, "r+").read())
    cipher = PKCS1_OAEP.new(privateKey)
    return cipher.encrypt(message)

def myIP():
    new = open(IP, "r+")
    ip = new.readline().strip("\n")
    new.close()
    return ip


def guardarLlave():
    publicKey = RSA.generate(1024)
    end = open(PUBLIC_KEY, "w")
    end.write(publicKey.exportKey().decode('utf-8'))
    end.close()


server()

# docker build -t face .
# docker run -p 15951:15951 -v /home/wagcm/Escritorio/Tarea2_SO/carpetaDocker:/carpetaDocker face