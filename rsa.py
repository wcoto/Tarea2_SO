from Crypto.PublicKey import RSA
from Crypto.Util import randpool

rand = randpool.RandomPool()
RSAKey = RSA.generate(1024, rand.get_bytes)
publickey = RSAKey.publickey() # pub key export for exchange
encrypted = publickey.encrypt("hola".encode('utf-8'), 32)
#message to encrypt is in the above line 'encrypt this message'

print ('encrypted message: ', encrypted) #ciphertext
decrypted = RSAKey.decrypt(encrypted)
print ('\ndecrypted', decrypted)
