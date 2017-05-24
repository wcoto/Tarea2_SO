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

# Creates a new server
def server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
    except (socket.error):
        print ("\nFallo en el enlace...")
        sys.exit()

    server.listen(10)
    print("\n\nServidor esperando clientes...")

    while True:
        conn, addr = server.accept()
        if(trustedHost(addr[0]) == True): #Analyse if the client is trusted
            print ("\nConectado con: " + addr[0] + ":" + str(addr[1]))
            data = conn.recv(1024)
            message = concatMessage(decryptar(data).decode("utf-8")) #Decrypt and link with the local message
            print("Message:", message)
            if (message != "ready"): #Analyse if the message have finished
                data = encryptar(message.encode('utf-8')) #Encrypt the current message
                clientSend(data) # Send the data by the socket client
            conn.close()
        else:
            conn.send("\nSu conexion no es permitida en este sistema\n".encode())
            conn.close()
    server.close()

# Sends a message to next server
def clientSend(data):
    indexNextServer = ipIndex() + 1 #Search the next ip port to send the message
    ipList = createIPList()
    client = socket.socket()
    client.connect((ipList[indexNextServer], EXTERN_PORT))
    client.send(data)
    client.close()

# Looking for the index of current ip machine
def ipIndex():
    ipList = createIPList()
    return ipList.index(myIP())

# Creates a list with the ip trusted machines
def createIPList():
    ipList = []
    with open(CONFIG, "r+") as reader:
        for line in reader:
            ipList.append(line.strip("\n"))
    reader.close()
    return ipList

# Returns True if the incomming client is trusted, else otherwise
def trustedHost(host):
    ipList = createIPList()
    return host in ipList

# Returns True if the message contains the CONDITIONAL word into
def isFin(message):
    results = message.split(" ")
    valor = False
    for i in results:
        if (i == CONDITIONAL):
            valor = True
    return valor

# Link the message with the local word or stores it into file
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

# Decrypt the received message
def decryptar(encryptedMessage):
    privateKey = RSA.importKey(open(PUBLIC_KEY, "r+").read())
    cipher = PKCS1_OAEP.new(privateKey)
    return cipher.decrypt(encryptedMessage)

# Encrypt the current message to send it by socket
def encryptar(message):
    privateKey = RSA.importKey(open(PUBLIC_KEY, "r+").read())
    cipher = PKCS1_OAEP.new(privateKey)
    return cipher.encrypt(message)

# Returns the local ip, which is allocated into a local file
def myIP():
    new = open(IP, "r+")
    ip = new.readline().strip("\n")
    new.close()
    return ip

# Creates a new random key and stores it into a local file
def guardarLlave():
    publicKey = RSA.generate(1024)
    end = open(PUBLIC_KEY, "w")
    end.write(publicKey.exportKey().decode('utf-8'))
    end.close()

# Runs the server
server()

# docker build -t tarea2 .
# docker run -p 15951:15951 -v /home/wagcm/Escritorio/Tarea2_SO/carpetaDocker:/carpetaDocker tarea2