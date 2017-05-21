#! /usr/bin/python
print ("Programa que compara host\n")
fo = open("/carpetaDocker/mensaje.txt", "r+")
str = fo.read(25);
print "La informacion es : ", str
fo.close()

def trustedHost(host):
	with open("/carpetaDocker/Configuracion.config", "r+") as reader:
		valor = False;
		for line in reader:
			if line.strip("\n") == host:
				valor = True
		return valor
	
print trustedHost("365.254.21.4")
