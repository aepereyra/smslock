#!/usr/bin/env python
import humod
import RPi.GPIO as GPIO
import time

class MyModem(humod.Modem):
    def sms_list_by_num(self):
        """Lists messages from a particular sender."""
        messages = []
	booleano = 'false'
        for message in self.sms_list():
		#busco en el archivo accesslist si el telefono esta habilitado
		if message[2] in open('accesslist').read():
        		messages.append(message)
			#imprimo los datos en pantalla puede ir a un log
			print messages
			#devuelvo true si estaba habilitado
			booleano = 'true'
	return booleano
#defino el modem
modem = MyModem()
#habilito la recepcion de mensajes
modem.enable_textmode(True)
#ciclo infinito 
while 1==1:
	time.sleep(1) 
	mensaje = modem.sms_list_by_num()
	#si la funcion devuelve true enciendo el gpio17
	if mensaje == 'true':
		#creo que esta de mas este print
		print mensaje
		GPIO.setmode(GPIO.BOARD)
                GPIO.setup(11, GPIO.OUT)
                GPIO.output(11,True)
		#despues de 4 segundos lo apago
                time.sleep(4)
                GPIO.output(11,False)
		msj = []
		#elimino los mensajes que tiene el modem por ahi habria que hacerlo cada vez que llega un msj
		for msj in modem.sms_list():
     			modem.sms_del(msj[0])
