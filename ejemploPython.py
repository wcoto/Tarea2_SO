#! /usr/bin/python
print ("Programa que lee archivo de texto\n")
fo = open("/carpetaDocker/mensaje.txt", "r+")
str = fo.read(25);
print "La informacion es : ", str
fo.close()

def trustedHost(host):
	with open("/carpetaDocker/Configuracion.config", "r+") as reader:
		for line in reader:
			print line.strip("\n") == host
	
trustedHost("365.254.21.4")
