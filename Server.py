import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 9992))
s.listen(1)

        sc, addr = s.accept()


while True:
      recibido = sc.recv(1024)
      if recibido == "quit":
         break
      print "Recibido:", recibido
      sc.send(recibido)

print "adios"

sc.close()
s.close()

# gethostbyname(gethostname())
# https://stackoverflow.com/questions/35384437/socket-connection-over-internet-in-python


message = 'To be encrypted'
>>> key = RSA.importKey(open('pubkey.der').read())
>>> cipher = PKCS1_OAEP.new(key)
>>> ciphertext = cipher.encrypt(message)


>>> key = RSA.importKey(open('privkey.der').read())
>>> cipher = PKCS1_OAP.new(key)
>>> message = cipher.decrypt(ciphertext)


#def encryptar(message):
    #publickey = RSA.generate(1024)
    #print ("Public: ", publickey.exportKey())
    #cipher_rsa = PKCS1_OAEP.new(publickey)
    #encrypted = cipher_rsa.encrypt(message.encode('utf-8'))
    #print ('\nEncrypted message: ', encrypted)
    #decrypted = cipher_rsa.decrypt(encrypted)
    #print ('\nDecrypted message', decrypted)


# telnet 192.168.100.10 15951


            print ("Mensaje para enviar: ", message)
            clientSend(message)



                        data = encryptar(key, message)
            print ("Encriptado: ", data)