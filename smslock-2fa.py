#!/usr/bin/env python
import humod
import RPi.GPIO as GPIO
import time
import sqlite3
import sys
import hashlib

def limpia(self):
	msj = []
	for msj in modem.sms_list():
        	modem.sms_del(msj[0])
	return 0

class MyModem(humod.Modem):
    def sms_list_by_num(self):
        messages = []
	booleano = 'false'
	conn = sqlite3.connect('accesslist.db')
        for message in self.sms_list():
		with conn:
		     cursor =  conn.execute("SELECT * FROM USUARIO")
		     for row in cursor:
			 if message[2] == row[0]:
	                        messages.append(message)
        	                #imprimo los datos en pantalla puede ir a un log
				print messages
				#bajo los mensajes para leer el cuerpo del mensaje
				clave= self.sms_read(0)
				clavehash = hashlib.sha512(clave).hexdigest()
				if clavehash == row[1]:
					#devuelvo true si estaba habilitado
                       			booleano = 'true'
					print "Clave Correcta"

	return booleano

GPIO.setwarnings(False)
#defino el modem
modem = MyModem()
#habilito la recepcion de mensajes
modem.enable_textmode(True)
#limpio mensajes en memoria
limpia(0)
#ciclo infinito
while 1:
	time.sleep(1) 
	mensaje = modem.sms_list_by_num()
	#si la funcion devuelve true enciendo el gpio17
	if mensaje == 'true':
		GPIO.setmode(GPIO.BOARD)
                GPIO.setup(11, GPIO.OUT)
                GPIO.output(11,True)
		#despues de 4 segundos lo apago
                time.sleep(4)
                GPIO.output(11,False)
		#elimino los mensajes que tiene guardados
		limpia(0)
	#Esta llamada a limpiar deberia chequear antes que haya llegado un mensaje 
	#Sirve para limpiar mensajes de telefonos sin permisos e impide que se llene la memoria sim con basura
	limpia(0)


