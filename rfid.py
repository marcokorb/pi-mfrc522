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
	
	def write(self, text):
		
		tag_id, tag_text = self.reader.write_no_block(text)
		
		if tag_id is None:
			
			tag_id, tag_text = self.reader.write_no_block(text)
			
		return tag_id, tag_text
			
	def read_no_block(self):
		
		tag_id, tag_text = self.reader.read_no_block()
		
		if tag_id is None:
			
			tag_id, tag_text = self.reader.read_no_block()
			
		return tag_id, tag_text
			
