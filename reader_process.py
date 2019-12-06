# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

from rfid import RFID

GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

rfid = RFID()

while True:
	
	#try:
				
		tag_id = rfid.reader.read_id_no_block()
			
		if tag_id == 989699569615:
			GPIO.output(8, GPIO.HIGH)
		else:
			GPIO.output(8, GPIO.LOW)
		
	#finally:
#		pass
		
GPIO.cleanup()	
