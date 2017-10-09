# -*- coding: utf-8 -*-
from random import randint

class Die( ):
	"""表示一个筛子的类"""
	def __init__(self, num_sides=6):
		"""默认为6点所在面"""
		self.num_sides = num_sides

	def roll(self):
		"""返回一个1-6之间的随机数值"""
		return randint(1,self.num_sides)
		