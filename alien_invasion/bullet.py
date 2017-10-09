# -*- coding: utf-8 -*-

# 子弹类

import pygame 
from pygame.sprite import Sprite

class  Bullet(Sprite):
	"""飞船发送的子弹管理的类"""
	def __init__(self, ai_settings,screen,ship):
		super( Bullet, self).__init__()
		self.screen = screen
		
		# 在(0,0)处 创建一个表示子弹的矩形,在设置正确的位置
		self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)

		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		# 存储用小数点表示的子弹位置
		self.y = float(self.rect.y) 

		# 设置颜色和速度
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
		
	def update(self):
		"""向上移动子弹"""
		self.y -= self.speed_factor
		self.rect.y = self.y

	def draw_bullet(self):
		"""屏幕上 绘制子弹"""
		pygame.draw.rect(self.screen,self.color,self.rect)
