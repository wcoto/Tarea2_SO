#! /usr/bin/python
print ("Programa que lee archivo de texto\n")
fo = open("/carpetaDocker/mensaje.txt", "r+")
str = fo.read(10);
print "La informacion es : ", str
fo.close()

