# -*- coding: utf-8 -*-

from car import Car

class  Person():
	"""定义一个Person类"""
	def __init__(self, name,age):
		self.name = name
		self.age = age
	def  info(self):
		print("[Person ]name:"+self.name+" age:"+str(self.age))
		pass

# 定义一个Studen 类
class  Student(Person):
	"""定义一个Student类继承Person类"""
	def __init__(self, name,age,studenId):
		super().__init__(name,age)
		self.studenId = studenId

	def info(self):
		print("[Student] name:"+self.name+" age:"+str(self.age)+" id:"+self.studenId)

# 定义一个Teacher类

class Teacher(Person):
	"""定义一个Teacher类继承Person"""
	def __init__(self, name,age,teacherID):
		super(Teacher, self).__init__(name,age)
		self.teacherID = teacherID

	def info(self):
		print("[Teacher] name:"+self.name+" age:"+str(self.age )+" id:"+self.teacherID)


