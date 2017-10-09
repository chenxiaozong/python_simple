# -*- coding: utf-8 -*-
# 使用类的继承
class Car( ):
	"""一次模拟汽车类的尝试"""
	def __init__(self, make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		long_name = str(self.year)+' '+self.make+" "+ self.model
		return long_name
	def  read_odometer(self):
		print("this car has "+ str(self.odometer_reading)+" miles on it")
	def update_odometer(self,mileage):
		if mileage>=self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("you can't roll back an odometer ")
	def increment_odometer(self,miles):
		self.odometer_reading +=miles
	def fill_gas(self):
		print("fill gas....")
		pass
		











































































































