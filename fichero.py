#!/usr/bin/python3
#ANA MARÍA GONZÁLEZ DÍAZ

file = open('/etc/passwd','r')
lines = file.readlines()

dictionary = {}
for line in lines:
	item = line.split(':')
	user = item[0]
	shell = item[-1]
	print('Usuario:',user,' Shell:',shell)
	dictionary[user] = shell

try:
	print('root',dictionary['root'])
	print('imaginario',dictionary['imaginario'])
except:	
	print('Error al enconctrar el usuario en el diccionario')
file.close()
