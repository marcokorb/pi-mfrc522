# -*- coding: utf-8 -*-

__all__ = ['RFID']


from mfrc522 import SimpleMFRC522

from utils import gpio_wrapper


class RFID(object):
	
	def __init__(self):
		
		self.reader = SimpleMFRC522()
	
	@gpio_wrapper
	def read(self):		
		
		return self.reader.read_no_block()
	
	@gpio_wrapper	
	def write(self, text):
		
		return self.reader.write_no_block(text)
	
	def unwrapped_read(self):
		
		return self.reader.read_no_block()
