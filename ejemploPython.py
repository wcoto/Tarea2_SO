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
concatMessage("Son Dos Tres Cuatro Cinco fin")
