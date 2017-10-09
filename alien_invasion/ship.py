# 创建ship 类管理飞船的大部分行为


import pygame

from pygame.sprite import Sprite


class Ship(Sprite):
	def __init__(self,ai_settings, screen):
		"""初始化飞船,并设置其初始位置"""
		super(Ship, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		"""加载飞船图像,并获取其外接举行"""

		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()


		self.move_step = self.ai_settings.ship_speed_factor #左右移动步长

		#移动标志位
		self.moving_right = False
		self.moving_left = False



		# 将新飞船 放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image,self.rect)


	def update(self):
		"""根据移动标志位,调整飞船位置"""
		if self.moving_right :
			self.rect.centerx +=self.move_step

			if self.rect.centerx > self.screen_rect.right:
				self.rect.centerx = self.screen_rect.right

		if self.moving_left:
			self.rect.centerx -=self.move_step

			if self.rect.centerx < 0:
				self.rect.centerx = 0

	def center_ship(self):
		"""让飞船在屏幕上居中"""
		self.center = self.screen_rect.centerx
		# self.rect.bottom = self.screen_rect.bottom

