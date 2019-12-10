# -*- coding: utf-8 -*-

__all__ = ['LCD']

import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd


# Modify this if you have a different sized character LCD
lcd_columns = 16
lcd_rows = 2
 
# Metro M0/M4 Pin Config:
lcd_rs = digitalio.DigitalInOut(board.D6)
lcd_en = digitalio.DigitalInOut(board.D24)
lcd_d7 = digitalio.DigitalInOut(board.D22)
lcd_d6 = digitalio.DigitalInOut(board.D18)
lcd_d5 = digitalio.DigitalInOut(board.D17)
lcd_d4 = digitalio.DigitalInOut(board.D23)
lcd_backlight = digitalio.DigitalInOut(board.D2)


class LCD(object):
	
	def __init__(self):
		
		self.lcd = characterlcd.Character_LCD_Mono(
			lcd_rs,
			lcd_en,
			lcd_d4,
			lcd_d5,
			lcd_d6,
			lcd_d7,
			lcd_columns,
			lcd_rows,
			lcd_backlight
		)
		
		self.lcd.backlight = False
		
	def write(self, text):
		
		self.lcd.message = text
		
	def clear(self):
		
		self.lcd.clear()
