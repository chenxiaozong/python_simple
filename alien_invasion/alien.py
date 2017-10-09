# -*- coding: utf-8 -*-

# 外星人对应的类

import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
	"""表示单个外星人的类"""

	def __init__(self, ai_settings,screen):
		super(Alien, self).__init__()
		self.ai_settings = ai_settings
		self.screen = screen
		
		# 加载外星人图片
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		# 初始化:每个外星人最初都在屏幕左上角附近
		# self.rect.x = self.rect.width
		# self.rect.y = self.rect.height
		self.rect.x = self.rect.width
		self.rect.y = 0

		# 存储外星人的准确位置
		self.x = float(self.rect.x)
	def blitme(self):
		"""在指定位置绘制外星人"""
		self.screen.blit(self.image,self.rect)

	def update(self):
		"""向右移动外星人"""
		self.x+=(self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
		self.rect.x = self.x


	def check_fleet_edges(self):
		"""如果外星人位于屏幕的边缘,返回True"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <=0:
			return True

