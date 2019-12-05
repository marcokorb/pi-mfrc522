# -*- coding: utf-8 -*-

__all__ = ['gpio_wrapper']

import RPi.GPIO as GPIO


def gpio_wrapper(fn):

	def decorator(*args, **kwargs):
		
		result = None
	
		try:		
		
			result = fn(*args, **kwargs)
			
		finally:
		
			GPIO.cleanup()
		
		return result
		
	return decorator
		
			
