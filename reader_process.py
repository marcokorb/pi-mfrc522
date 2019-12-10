# -*- coding: utf-8 -*-

import board
import socket
import digitalio
import time

from lcd import LCD
from rfid import RFID

lcd = LCD()

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT


def get_ip_address():
	ip_address = ''
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8",80))
	ip_address = s.getsockname()[0]
	s.close()
	return ip_address

rfid = RFID()

host_ip = get_ip_address()

while True:
	
	tag_id, tag_text = rfid.read_no_block()
	
	print(tag_id)
	
	lcd.clear()
	
	if tag_id is None:		
		lcd.write(host_ip)
		led.value = False			
	else:
		lcd.write(tag_text)
		if tag_id == 989699569615:
			
			led.value = True
		
GPIO.cleanup()	
